from testtools import TestCase

from solaredge.params import decode_parameters


class TestDecodeParameter(TestCase):

    def test_uint(self):
        self.assertEqual(
            [1234], decode_parameters(b'\xd2\x04\x00\x00\x00\x00'))
        self.assertEqual(
            [12345678], decode_parameters(b'\x4e\x61\xbc\x00\x00\x00'))

    def test_int(self):
        self.assertEqual(
            [-10], decode_parameters(b'\xf6\xff\xff\xff\x02\x00'))
        self.assertEqual(
            [-12345678], decode_parameters(b'\xb2\x9e\x43\xff\x02\x00'))

    def test_float(self):
        self.assertEqual(
            [-123.3],
            [round(f, 1)
             for f in decode_parameters(b'\x9a\x99\xf6\xc2\x01\x00')])
        self.assertEqual(
            [12345678], decode_parameters(b'\x4e\x61\x3c\x4b\x01\x00'))

    def test_string(self):
        self.assertEqual(
            [b'foo'], decode_parameters(b'\x00\x00\x00\x00\x03\x00foo\x00'))
        # Though the value is almost always zero, it's occasionally not.
        # But it doesn't seem significant.
        self.assertEqual(
            [b'quux'], decode_parameters(b'\x02\x00\x00\x00\x03\x00quux\x00'))

    def test_multiple(self):
        self.assertEqual(
            [b'foo', 1234, 12345678],
            decode_parameters(
                b'\x00\x00\x00\x00\x03\x00foo\x00'
                b'\xd2\x04\x00\x00\x00\x00'
                b'\x4e\x61\x3c\x4b\x01\x00'))
