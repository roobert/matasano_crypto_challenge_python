#!/usr/bin/env python3
#
# 6. Break repeating-key XOR
#
# The buffer at the following location:
#
#  https://gist.github.com/3132752
#
# is base64-encoded repeating-key XOR. Break it.
#
# Here's how:
#
# a. Let KEYSIZE be the guessed length of the key; try values from 2 to
# (say) 40.
#
# b. Write a function to compute the edit distance/Hamming distance
# between two strings. The Hamming distance is just the number of
# differing bits. The distance between:
#
#   this is a test
#
# and:
#
#   wokka wokka!!!
#
# is 37.
#
# c. For each KEYSIZE, take the FIRST KEYSIZE worth of bytes, and the
# SECOND KEYSIZE worth of bytes, and find the edit distance between
# them. Normalize this result by dividing by KEYSIZE.
#
# d. The KEYSIZE with the smallest normalized edit distance is probably
# the key. You could proceed perhaps with the smallest 2-3 KEYSIZE
# values. Or take 4 KEYSIZE blocks instead of 2 and average the
# distances.
#
# e. Now that you probably know the KEYSIZE: break the ciphertext into
# blocks of KEYSIZE length.
#
# f. Now transpose the blocks: make a block that is the first byte of
# every block, and a block that is the second byte of every block, and
# so on.
#
# g. Solve each block as if it was single-character XOR. You already
# have code to do this.
#
# e. For each block, the single-byte XOR key that produces the best
# looking histogram is the repeating-key XOR key byte for that
# block. Put them together and you have the key.

import sys
import os
DIR_PATH = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.join(DIR_PATH, "../lib"))

import unittest
from binascii import hexlify
from pprint import pprint
from xor import *
from break_repeating_xor_key import *
from detect_single_character_xor import *
from results import *

class TestChallenge6(unittest.TestCase):
    with open(os.path.join(DIR_PATH, "data/6.txt"), encoding="ISO-8859-1") as file:
        data = file.read()

    encrypted_bytes = b64decode(data)

    def test_hamming_distance(self):
        self.assertEqual(hamming_distance(b"this is a test", b"wokka wokka!!!"), 37)

    def test_minimum_hamming_distances(self):
        # NOTE: could potentially calculate hamming distance range from cipher text length..
        results = minimum_hamming_distances(self.encrypted_bytes, range(2,41))

        self.assertEqual(find_min(results, "normalized_hamming_distance")["keysize"], 29)

    def test_transpose(self):
        bytes = "abcdefghijkl"
        target = [['a', 'd', 'g', 'j'], ['b', 'e', 'h', 'k'], ['c', 'f', 'i', 'l']]

        self.assertEqual(transpose(bytes, 3), target)

    def test_challenge6(self):
        # number of bytes: 2871
        # block size: 29
        # number of blocks: 99
        # padding: 24 

        # block size calculated by prior hamming distance test..
        blocks = transpose(self.encrypted_bytes, 29)

        collection = []

        for block in blocks:
            # FIXME: score() should take bytes not hex
            collection.append(find_max(score(hexlify(bytes(block))), "score"))

        key = ""
        for data in collection:
            key += data["key"]

        decrypted_message = repeating_xor(self.encrypted_bytes, key.encode("ASCII"))

        with open(os.path.join(DIR_PATH, "data/6-decrypted.txt"), encoding="ISO-8859-1") as file:
            target = file.read()

        self.assertEqual(decrypted_message.decode("ASCII"), target)

if __name__ == '__main__':
    unittest.main()
