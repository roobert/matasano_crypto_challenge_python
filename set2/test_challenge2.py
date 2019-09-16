#!/usr/bin/env python3
# 2. Implement CBC mode
#
# CBC mode is a block cipher mode that allows us to encrypt irregularly-sized 
# messages, despite the fact that a block cipher natively only transforms individual 
# blocks.
# 
# In CBC mode, each ciphertext block is added to the next plaintext block before 
# the next call to the cipher core.
# 
# The first plaintext block, which has no associated previous ciphertext block, 
# is added to a "fake 0th ciphertext block" called the initialization vector, or IV.
# 
# Implement CBC mode by hand by taking the ECB function you wrote earlier, making 
# it encrypt instead of decrypt (verify this by decrypting whatever you encrypt 
# to test), and using your XOR function from the previous exercise to combine them.
# 
# The file here is intelligible (somewhat) when CBC decrypted against "YELLOW SUBMARINE" 
# with an IV of all ASCII 0 (\x00\x00\x00 &c)

import sys
import os
DIR_PATH = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.join(DIR_PATH, "../lib"))

import unittest
from base64 import b64decode
from padding import *
from ecb import *

class TestChallenge2(unittest.TestCase):
    with open(os.path.join(DIR_PATH, "../set2/data/10.txt"), encoding="ISO-8859-1") as file:
        data = file.read()

    with open(os.path.join(DIR_PATH, "../set2/data/10-decrypted.txt"), encoding="ISO-8859-1") as file:
        target = file.read()

    def test_decrypt_ecb_cbc(self):
        text = b"abcdefghijklmnopqrstu"
        iv  = b"iviviviviviviviv"
        key = b"xxxxxxxxxxxxxxxx"

        cipher_text = encrypt_ecb_cbc(text, key, iv)

        self.assertEqual(text, (decrypt_ecb_cbc(cipher_text, key, iv)))

    def test_challenge2(self):
        key = b"YELLOW SUBMARINE"
        iv = b"\x00" * 16
        self.assertEqual(self.target, decrypt_ecb_cbc(b64decode(self.data), key, iv).decode("ASCII"))

if __name__ == '__main__':
    unittest.main()
