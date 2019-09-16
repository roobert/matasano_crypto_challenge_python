#!/usr/bin/env python3
#
# 8. Detecting ECB
#
# At the following URL are a bunch of hex-encoded ciphertexts:
#
#    https://gist.github.com/3132928
#
# One of them is ECB encrypted. Detect it.
#
# Remember that the problem with ECB is that it is stateless and
# deterministic; the same 16 byte plaintext block will always produce
# the same 16 byte ciphertext.

import sys
import os
DIR_PATH = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.join(DIR_PATH, "../lib"))

import unittest
from pprint import pprint
from Crypto.Cipher import AES
from base64 import b64decode
from iteration_utilities import grouper
from results import *

class TestChallenge8(unittest.TestCase):
    with open(os.path.join(DIR_PATH, "data/8.txt"), encoding="ISO-8859-1") as file:
        data = file.readlines()

    target = "d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c74" \
            + "4cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2" \
            + "d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f" \
            + "4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af7" \
            + "0dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab" \
            + "51b29933f2c123c58386b06fba186a\n"

    def test_set8(self):
        # FIXME: replace with detect_ecb function 
        #        remember input needs to be array of bytes data..(non-b64 encoded)
        likely_ecb_texts = []
        line_number = 0

        # work out how many repeated chunks each entry has.
        # lots of repeated chunks means its likely ECB
        for line in self.data:
            line_number += 1

            chunks = {}

            # split line into 16 byte chunks since key is 16 bytes long
            for chunk in list(grouper(b64decode(line), 16)):
                if tuple(chunk) in chunks.keys():
                    chunks[tuple(chunk)] += 1
                else:
                    chunks[tuple(chunk)] = 0

            repeated_chunk_total = sum(chunks.values())

            if repeated_chunk_total == 0:
                continue

            likely_ecb_texts.append({
                "line_number": line_number,
                "cipher_text": line,
                "repeated_chunk_total": repeated_chunk_total
            })

        most_likely_ecb_text = find_max(likely_ecb_texts, "repeated_chunk_total")

        self.assertEqual(most_likely_ecb_text['cipher_text'], self.target)
        self.assertEqual(most_likely_ecb_text['line_number'], 133)
        self.assertEqual(most_likely_ecb_text['repeated_chunk_total'], 3)

if __name__ == '__main__':
    unittest.main()
