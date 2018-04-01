#!/usr/bin/python3

import asyncio
import logging
import sys

import solaredge.proto


class SolarEdgeMessageProtocol(asyncio.Protocol):

    _partial_message = b''
    transport = None
    closed = False

    def __init__(self):
        super().__init__()
        self._message_send_queue = []

    def connection_made(self, transport):
        self.transport = transport
        for msg in self._message_send_queue:
            self.send_message(msg)
        self._message_send_queue = []
        if self.closed:
            self.transport.close()

    def data_received(self, data):
        self._partial_message += data
        try:
            msg, tail = solaredge.proto.decode_message_with_tail(
                self._partial_message)
        except solaredge.proto.IncompleteMessageException:
            return
        except Exception:
            logging.exception("Bad message received.")
            self.close()
            return
        self._partial_message = tail
        self.message_received(msg)

    def send_message(self, msg):
        if self.transport is None:
            self._message_send_queue.append(msg)
        else:
            self.transport.write(solaredge.proto.encode_message(msg))

    def close(self):
        if self.transport is not None:
            self.transport.close()
        self.closed = True


class SolarEdgeEndpointProtocol(SolarEdgeMessageProtocol):

    def __init__(self, router, name):
        super().__init__()
        self.router = router
        self.name = name
        self.router.endpoints[name] = self

    def connection_made(self, transport):
        super().connection_made(transport)
        self.router.endpoint_connection_made(self.name)

    def connection_lost(self, exc):
        super().connection_lost(exc)
        self.router.endpoint_connection_lost(self.name)

    def message_received(self, msg):
        self.router.endpoint_message_received(self.name, msg)


class SolarEdgeMessageRouter:

    def __init__(self, loop):
        self.loop = loop
        self.endpoints = {}
        self.connect_handlers = []
        self.disconnect_handlers = []
        self.message_handlers = []

    def endpoint_connection_made(self, name):
        for handler in self.connect_handlers:
            handler(self, name)

    def endpoint_connection_lost(self, name):
        for handler in self.disconnect_handlers:
            handler(self, name)

    def endpoint_message_received(self, name, msg):
        for handler in self.message_handlers:
            handler(self, name, msg)


def connect_portal_when_device_connects(router, name):
    if not name.startswith('device-'):
        return
    portal_name = 'portal-{}'.format(name[7:])
    portal_proto = SolarEdgeEndpointProtocol(
        router, portal_name)

    async def connect_to_portal():
        try:
            await router.loop.create_connection(
                lambda: portal_proto, 'prod.solaredge.com', 22222)
        except Exception as e:
            logging.exception("Connection to SolarEdge portal failed.")
            router.endpoints[name].close()
    asyncio.ensure_future(connect_to_portal())


def forward_disconnect_between_portal_and_device(router, name):
    if name.startswith('device-'):
        device_idx = name[7:]
        router.endpoints['portal-{}'.format(device_idx)].close()
    if name.startswith('portal-'):
        device_idx = name[7:]
        router.endpoints['device-{}'.format(device_idx)].close()


def forward_message_between_portal_and_device(router, name, msg):
    if name.startswith('device-'):
        device_idx = name[7:]
        router.endpoints['portal-{}'.format(device_idx)].send_message(msg)
    if name.startswith('portal-'):
        device_idx = name[7:]
        router.endpoints['device-{}'.format(device_idx)].send_message(msg)


def debug_connect(router, name):
    print("{} connected".format(name))


def debug_disconnect(router, name):
    print("{} disconnected".format(name))


def debug_message(router, name, msg):
    print("{}: {}".format(name, msg))


LAST_DEVICE_IDX = 0


def get_device_idx():
    global LAST_DEVICE_IDX
    LAST_DEVICE_IDX += 1
    return LAST_DEVICE_IDX


def main(args):
    loop = asyncio.get_event_loop()
    router = SolarEdgeMessageRouter(loop)

    # Debug logging
    router.connect_handlers.append(debug_connect)
    router.disconnect_handlers.append(debug_disconnect)
    router.message_handlers.append(debug_message)

    # Device <-> portal
    router.connect_handlers.append(connect_portal_when_device_connects)
    router.disconnect_handlers.append(
        forward_disconnect_between_portal_and_device)
    router.message_handlers.append(forward_message_between_portal_and_device)

    server = loop.run_until_complete(loop.create_server(
        lambda: SolarEdgeEndpointProtocol(
            router, 'device-{}'.format(get_device_idx())),
        '0.0.0.0', 22222))
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()
    return 0


if __name__ == '__main__':
    main(sys.argv)