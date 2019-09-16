#!/usr/bin/env python3
#
# 2. Fixed XOR
#
# Write a function that takes two equal-length buffers and produces
# their XOR sum.
#
# The string:
#
#  1c0111001f010100061a024b53535009181c
#
# ... after hex decoding, when xor'd against:
#
#  686974207468652062756c6c277320657965
#
# ... should produce:
#
#  746865206b696420646f6e277420706c6179
#
# NOTE
#
# The key insight with XORing bits is that in the result, all bits that
# are *different* are 1, and all bits that are the *same* are 0

import sys
import os
DIR_PATH = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.join(DIR_PATH, "../lib"))

import unittest
from binascii import hexlify, unhexlify
from xor import *

class TestChallenge2(unittest.TestCase):
    buf_x = "1c0111001f010100061a024b53535009181c"
    buf_y = "686974207468652062756c6c277320657965"

    target = "746865206b696420646f6e277420706c6179"

    buf_x_bytes = unhexlify(buf_x)
    buf_y_bytes = unhexlify(buf_y)


    def test_challenge2(self):
        # encrypted text in plain english
        # print(self.buf_x_bytes)
        # => b'\x1c\x01\x11\x00\x1f\x01\x01\x00\x06\x1a\x02KSSP\t\x18\x1c'

        # encryption key in plain english
        # print(self.buf_y_bytes)
        # => b"hit the bull's eye"

        # target string in plain english
        # print(unhexlify(self.target))
        # => b"the kid don't play" 

        xor_result = xor(self.buf_x_bytes, self.buf_y_bytes)

        # xor result in plain english
        # print(xor_result)
        # => b"the kid don't play"

        # target is plain ascii so convert result for testing..
        self.assertEqual(self.target, hexlify(xor_result).decode("ASCII"))

if __name__ == '__main__':
    unittest.main()
