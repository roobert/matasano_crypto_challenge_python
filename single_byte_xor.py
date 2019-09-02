#!/usr/bin/env python

import sys
import operator
import binascii
from pprint import pprint
from helpers import *

def frequency_table():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .,!'?"
    frequencies = [
        11.602, 4.702,  3.511,
        2.670,  2.000,  3.779,
        1.950,  7.232,  6.286,
        0.631,  0.690,  2.705,
        4.374,  2.365,  6.264,
        2.545,  0.173,  1.653,
        7.755,  16.671, 1.487,
        0.619,  6.661,  0.005,
        1.620,  0.050,
        11.602, 4.702,  3.511,
        2.670,  2.000,  3.779,
        1.950,  7.232,  6.286,
        0.631,  0.690,  2.705,
        4.374,  2.365,  6.264,
        2.545,  0.173,  1.653,
        7.755,  16.671, 1.487,
        0.619,  6.661,  0.005,
        1.620,  0.050,  20,
        0.500,  0.500,  0.500,
        0.500,  0.500
    ]

    character_bytes = characters.encode("ISO-8859-1")
    character_frequency_table = dict(zip(character_bytes, frequencies))

    return character_frequency_table

def generate_results(message):

    results = []

    # ASCII range
    for key in range(256):
        #print("key: " + chr(key))

        # create a string of characters in bytes to xor message against
        xor_buffer = (chr(key) * len(message)).encode("ISO-8859-1")

        xor_result = xor(binascii.unhexlify(message), xor_buffer)

        #print("input:   " + message)
        #print("output:  " + xor_buffer.decode("ISO-8859-1"))
        #print("target:  " + binascii.hexlify(target.encode("ISO-8859-1")).decode("ISO-8859-1"))
        #print("xor hex: " + xor_result.hex())
        #print("xor:     " + xor_result.decode("ISO-8859-1"))

        #print()

        # calculate score based on frequency of characters in sentence
        score = 0
        for char in xor_result:
            try:
                score += frequency_table()[char]
            except:
                pass

        result = {}
        result["score"] = score
        result["message"] = xor_result.decode("ISO-8859-1")
        result["key"] = chr(key)

        results.append(result)

    return results

def max_score_result(results):
    return max(results, key=lambda x:x['score'])

# find most likely key for encrypted data
#pprint(max_score_result(generate_results())["key"])
