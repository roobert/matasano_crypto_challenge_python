#!/usr/bin/env python3
#
# 4. Byte-at-a-time ECB decryption, Full control version
#
# Copy your oracle function to a new function that encrypts buffers
# under ECB mode using a consistent but unknown key (for instance,
# assign a single random key, once, to a global variable).
#
# Now take that same function and have it append to the plaintext,
# BEFORE ENCRYPTING, the following string:
#
#   Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
#   aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
#   dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
#   YnkK
#
# SPOILER ALERT: DO NOT DECODE THIS STRING NOW. DON'T DO IT.
#
# Base64 decode the string before appending it. DO NOT BASE64 DECODE THE
# STRING BY HAND; MAKE YOUR CODE DO IT. The point is that you don't know
# its contents.
#
# What you have now is a function that produces:
#
#   AES-128-ECB(your-string || unknown-string, random-key)
#
# You can decrypt "unknown-string" with repeated calls to the oracle
# function!
#
# Here's roughly how:
#
# a. Feed identical bytes of your-string to the function 1 at a time ---
# start with 1 byte ("A"), then "AA", then "AAA" and so on. Discover the
# block size of the cipher. You know it, but do this step anyway.
#
# b. Detect that the function is using ECB. You already know, but do
# this step anyways.
#
# c. Knowing the block size, craft an input block that is exactly 1 byte
# short (for instance, if the block size is 8 bytes, make
# "AAAAAAA"). Think about what the oracle function is going to put in
# that last byte position.
#
# d. Make a dictionary of every possible last byte by feeding different
# strings to the oracle; for instance, "AAAAAAAA", "AAAAAAAB",
# "AAAAAAAC", remembering the first block of each invocation.
#
# e. Match the output of the one-byte-short input to one of the entries
# in your dictionary. You've now discovered the first byte of
# unknown-string.
#
# f. Repeat for the next byte.

import sys
sys.path.append('../lib')

import unittest
import time
import re
from pprint import pprint
from random import randint
from base64 import *
from padding import *
from ecb import *
from key import *
from oracle import *


class TestChallenge4(unittest.TestCase):
    secret = b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg" \
           + "aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq" \
           + "dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg" \
           + "YnkK")

    # consistent but *unknown* key
    with open("../set2/data/12-key.txt", encoding="ISO-8859-1") as file:
        key = b64decode(file.read())

    oracle_context = {
        "key": key,
        "secret": secret
    }

    def test_ecb_blocksize(self):
        # FIXME: write this
        True

    def test_challenge4(self):
        plain_text = break_ecb_byte_by_byte(self.oracle_context)
        self.assertEqual(plain_text, self.oracle_context["secret"])

if __name__ == '__main__':
    unittest.main()
