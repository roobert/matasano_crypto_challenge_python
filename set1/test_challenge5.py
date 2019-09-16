#!/usr/bin/env python3
#
# 5. Repeating-key XOR Cipher
#
# Write the code to encrypt the string:
#
#   Burning 'em, if you ain't quick and nimble
#   I go crazy when I hear a cymbal
#
# Under the key "ICE", using repeating-key XOR. It should come out to:
#
#   0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
#
# Encrypt a bunch of stuff using your repeating-key XOR function. Get a
# feel for it.

import sys
import os
DIR_PATH = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.join(DIR_PATH, "../lib"))

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
