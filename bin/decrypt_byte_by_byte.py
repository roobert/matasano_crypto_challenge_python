#!/usr/bin/env python3

# for fun!

import sys
import os
DIR_PATH = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.join(DIR_PATH, "../lib"))

import time
import re
from base64 import *
from ecb import *

secret = b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg" \
       + "aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq" \
       + "dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg" \
       + "YnkK")

# consistent but *unknown* key
with open(os.path.join(DIR_PATH, "../set2/data/12-key.txt"), encoding="ISO-8859-1") as file:
    key = b64decode(file.read())

oracle_context = {
    "key": key,
    "secret": secret
}

print()
print("  ECB byte by byte decryption ")
print()

t_start = time.perf_counter()

fast = not(len(sys.argv) > 1 and sys.argv[1] == "--fast")

plain_text = break_ecb_byte_by_byte(oracle_context, fast).decode("ASCII")

t_stop = perf_counter()

print("    *  decrypting done in {:2.3f} seconds".format(t_stop - t_start))
print()
print("  * decrypted cipher text:")
print()

for line in plain_text.splitlines():
    print("      " + line)
