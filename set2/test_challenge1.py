#!/usr/bin/env python3
#
# 1. Implement PKCS#7 padding
#
# Pad any block to a specific block length, by appending the number of
# bytes of padding to the end of the block. For instance,
#
#   "YELLOW SUBMARINE"
#
# padded to 20 bytes would be:
#
#   "YELLOW SUBMARINE\x04\x04\x04\x04"
#
# The particulars of this algorithm are easy to find online.

import sys
import os
DIR_PATH = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.join(DIR_PATH, "../lib"))

import unittest
from padding import *

class TestChallenge1(unittest.TestCase):
    def test_pad(self):
        self.assertEqual(pad(b"abcd", 3), b"abcd\x02\x02")
        self.assertEqual(pad(b"abcd", 4), b"abcd\x04\x04\x04\x04")
        self.assertEqual(pad(b"abcd", 5), b"abcd\x01")
        self.assertEqual(pad(b"abcd", 8), b"abcd\x04\x04\x04\x04")
        self.assertRaises(Exception, pad, b"abcd", 256)

    def test_challenge1(self):
        self.assertEqual(pad(b"YELLOW SUBMARINE", 20), b"YELLOW SUBMARINE\x04\x04\x04\x04")

if __name__ == '__main__':
    unittest.main()
