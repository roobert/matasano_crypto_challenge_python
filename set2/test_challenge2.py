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
sys.path.append('../lib')

import unittest
from padding import *
from ecb import *

class TestChallenge2(unittest.TestCase):
    with open("../set2/data/10.txt", encoding="ISO-8859-1") as file:
        data = file.read()

    #def test_decrypt_ecb_cbc(self):
    #    # 21 bytes
    #    text = b"abcdefghijklmnopqrstu"

    #    # 16 bytes
    #    iv  = b"iviviviviviviviv"
    #    key = b"xxxxxxxxxxxxxxxx"

    #    cipher_text = encrypt_ecb_cbc(text, key, iv)

    #    self.assertEqual(text, (decrypt_ecb_cbc(cipher_text, key, iv)))

    def test_challenge2(self):
        key = b"YELLOW SUBMARINE"
        iv = b"\x00" * 16
        print(decrypt_ecb_cbc(self.data.encode("ASCII"), key, iv).decode("ASCII"))

    #    self.assertEqual(pad(b"YELLOW SUBMARINE", 20), b"YELLOW SUBMARINE\x04\x04\x04\x04")
    #    #self.assertRaises(Exception, pad, b"abcd", 256)

if __name__ == '__main__':
    unittest.main()