#!/usr/bin/env python3
#
# 7. AES in ECB Mode
#
# The Base64-encoded content at the following location:
#
#     https://gist.github.com/3132853
#
# Has been encrypted via AES-128 in ECB mode under the key
#
#     "YELLOW SUBMARINE".
#
# (I like "YELLOW SUBMARINE" because it's exactly 16 bytes long).
#
# Decrypt it.
#
# Easiest way:
#
# Use OpenSSL::Cipher and give it AES-128-ECB as the cipher.

import sys
import os
DIR_PATH = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.join(DIR_PATH, "../lib"))

import unittest
from pprint import pprint
from Crypto.Cipher import AES
from base64 import b64decode

class TestChallenge7(unittest.TestCase):
    with open(os.path.join(DIR_PATH, "data/7.txt"), encoding="ISO-8859-1") as file:
        data = b64decode(file.read())

    with open(os.path.join(DIR_PATH, "data/7-decrypted.txt"), encoding="ISO-8859-1") as file:
        target = file.read().encode("ASCII") + b"\x04\x04\x04\x04"

    key = "YELLOW SUBMARINE"

    def test_set7(self):
        cipher = AES.new(self.key.encode("ASCII"), AES.MODE_ECB)
        data_decrypted = cipher.decrypt(self.data)

        # print(data_decrypted.decode("ASCII"))

        self.assertEqual(data_decrypted, self.target)

if __name__ == '__main__':
    unittest.main()
