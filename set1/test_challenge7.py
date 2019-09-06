#!/usr/bin/env python

import sys
sys.path.append('lib')

import unittest
from pprint import pprint
from Crypto.Cipher import AES
from base64 import b64decode

class TestChallenge6(unittest.TestCase):
    with open("data/7.txt", encoding="ISO-8859-1") as file:
        data = b64decode(file.read())

    with open("data/7-decrypted.txt", encoding="ISO-8859-1") as file:
        target = file.read().encode("ASCII") + b"\x04\x04\x04\x04"

    key = "YELLOW SUBMARINE"

    def test_set7(self):
        cipher = AES.new(self.key, AES.MODE_ECB)
        data_decrypted = cipher.decrypt(self.data)

        # print(data_decrypted.decode("ASCII"))

        self.assertEqual(data_decrypted, self.target)

if __name__ == '__main__':
    unittest.main()