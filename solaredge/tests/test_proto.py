import codecs

from testtools import TestCase
from testtools.matchers import MatchesStructure

import solaredge.proto


class TestEncodeDecodeMessage(TestCase):

    def test_no_data(self):
        raw = codecs.decode(
            '123456790000ffff2702efbeaddefeffffff0005b320', 'hex')
        msg = solaredge.proto.decode_message(raw)
        self.assertThat(
            msg,
            MatchesStructure.byEquality(
                seq=0x227,
                addr_from=0xdeadbeef,
                addr_to=0xfffffffe,
                type=0x500,
                data=b''))
        self.assertEqual(raw, solaredge.proto.encode_message(msg))

    def test_data(self):
        raw = codecs.decode(
            '123456791100eeff0c00efbeaddefdffffffd2044920616d206c6f7473206f66'
            '20646174612f69', 'hex')
        msg = solaredge.proto.decode_message(raw)
        self.assertThat(
            msg,
            MatchesStructure.byEquality(
                seq=0xc,
                addr_from=0xdeadbeef,
                addr_to=0xfffffffd,
                type=0x4d2,
                data=b'I am lots of data'))
        self.assertEqual(raw, solaredge.proto.encode_message(msg))
