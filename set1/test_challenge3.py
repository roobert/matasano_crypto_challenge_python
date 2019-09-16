#!/usr/bin/env python3
#
# 3. Single-character XOR Cipher
#
# The hex encoded string:
#
#       1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
#
# ... has been XOR'd against a single character. Find the key, decrypt
# the message.
#
# Write code to do this for you. How? Devise some method for "scoring" a
# piece of English plaintext. (Character frequency is a good metric.)
# Evaluate each output and choose the one with the best score.
#
# Tune your algorithm until this works.

import sys
import os
DIR_PATH = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.join(DIR_PATH, "../lib"))

import unittest
from pprint import pprint
from single_byte_xor import *
from results import *

class TestChallenge3(unittest.TestCase):
    message = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    target = "Cooking MC's like a pound of bacon"

    def test_challenge3(self):
        message = find_max(score(self.message), "score")["message"]

        self.assertEqual(self.target, message)

if __name__ == '__main__':
    unittest.main()
