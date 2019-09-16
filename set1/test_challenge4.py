#!/usr/bin/env python3
#
# 4. Detect single-character XOR
#
# One of the 60-character strings at:
#
#   https://gist.github.com/3132713
#
# has been encrypted by single-character XOR. Find it. (Your code from
# #3 should help.)

import sys
import os
DIR_PATH = os.path.join(os.path.dirname(__file__))
sys.path.append(os.path.join(DIR_PATH, "../lib"))

import unittest
from pprint import pprint
from single_byte_xor import *
from detect_single_character_xor import *
from results import *

class TestChallenge4(unittest.TestCase):
    data = open(os.path.join(DIR_PATH, "data/4.txt"), encoding="ISO-8859-1")
    target = "Now that the party is jumping\n"

    def test_challenge4(self):
        results = detect_single_character_xor(self.data)

        message_with_top_score = find_max(results, "score")

        self.assertEqual(self.target, message_with_top_score["message"])

if __name__ == '__main__':
    unittest.main()
