#!/usr/bin/env python

import sys
sys.path.append('../lib')

import unittest
from binascii import hexlify
from pprint import pprint
from xor import *

class TestChallenge5(unittest.TestCase):
    message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

    target = "0b3637272a2b2e63622c2e69692a23693a2a3c6324" \
            + "202d623d63343c2a26226324272765272a282b2f20" \
            + "430a652e2c652a3124333a653e2b2027630c692b20" \
            + "283165286326302e27282f"

    def test_challenge5(self):
        hex_bytes = hexlify(repeating_xor(self.message.encode("ASCII"), \
                "ICE".encode("ASCII")))

        self.assertEqual(self.target, hex_bytes.decode("ASCII"))

if __name__ == '__main__':
    unittest.main()
