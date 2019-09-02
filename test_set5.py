#!/usr/bin/env python

import unittest
import binascii
from helpers import *
from pprint import pprint

class TestSet5(unittest.TestCase):
    message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

    target = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272\na282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

    def test_set5(self):
        # FIXME: need to support multi-line 
        hex = binascii.hexlify(repeating_xor(self.message, "ICE")).decode("ASCII")

        self.assertEqual(self.target, hex)

if __name__ == '__main__':
    unittest.main()
