#!/usr/bin/env python3
#
# 3. Write an oracle function and use it to detect ECB.
#
# Now that you have ECB and CBC working:
#
# Write a function to generate a random AES key; that's just 16 random
# bytes.
#
# Write a function that encrypts data under an unknown key --- that is,
# a function that generates a random key and encrypts under it.
#
# The function should look like:
#
# encryption_oracle(your-input)
#  => [MEANINGLESS JIBBER JABBER]
#
# Under the hood, have the function APPEND 5-10 bytes (count chosen
# randomly) BEFORE the plaintext and 5-10 bytes AFTER the plaintext.
#
# Now, have the function choose to encrypt under ECB 1/2 the time, and
# under CBC the other half (just use random IVs each time for CBC). Use
# rand(2) to decide which to use.
#
# Now detect the block cipher mode the function is using each time.

import sys
import os
DIR_PATH = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.join(DIR_PATH, "../lib"))

import unittest
from pprint import pprint
from random import randint
from padding import *
from ecb import *
from key import *

class TestChallenge3(unittest.TestCase):
    with open(os.path.join(DIR_PATH, "../set2/data/10-decrypted.txt"), encoding="ISO-8859-1") as file:
        data = file.read()

    def test_challenge3(self):
        # NOTE: key length, iv, and block size should all match
        block_size = 16

        # NOTE: in order for this attack to work the plain text needs to have
        #       repeating blocks in it
        message = self.data.encode("ASCII")

        padding_length_prepend = randint(5, 10)
        padding_length_append = randint(5, 10)
        message = pad_random(message, padding_length_prepend, "prepend")
        message = pad_random(message, padding_length_append, "append")
        message = pad(message, block_size)

        key = random_key(block_size)

        if randint(1, 2) == 1:
            encryption = "ECB"
            cipher = AES.new(key, AES.MODE_ECB)
            cipher_text = cipher.encrypt(message)
        else:
            encryption = "ECB CBC"
            iv = random_key(block_size)
            cipher_text = encrypt_ecb_cbc(message, key, iv)

        data = {
                "encryption": encryption,
                "block_size": block_size,
                "padding": {
                    "appended": padding_length_append,
                    "prepended": padding_length_prepend,
                    },
                "cipher_text": cipher_text,
                "plain_text": message,
                }

        # if repeated blocks are detected in the cipher text then it is likely ECB mode
        if len(detect_ecb([cipher_text], block_size)) > 0:
            self.assertEqual(data["encryption"], "ECB")
        else:
            self.assertEqual(data["encryption"], "ECB CBC")

if __name__ == '__main__':
    unittest.main()
