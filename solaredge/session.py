import collections
import socket
import time

import solaredge.proto


# Hack to mostly ensure a sequence number that hasn't been used lately.
LAST_SEQ = int(time.time() * 10) % 32768

def get_seq():
    global LAST_SEQ
    LAST_SEQ += 1
    return LAST_SEQ


class Session:

    def __init__(self, tcp_address, local_addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(tcp_address)
        self.local_addr = local_addr

    def call(self, addr_to, message_type, message_data):
        seq = get_seq()
        self.sock.send(solaredge.proto.encode_message(solaredge.proto.Message(
            seq=seq, addr_from=self.local_addr, addr_to=addr_to,
            type=message_type, data=message_data))),
        resp_msg = solaredge.proto.decode_message(self.sock.recv(1024))
        assert resp_msg.seq == seq
        return resp_msg
