#!/usr/bin/python3
# Advent of code
# Day 5 - Part 1
import hashlib

input = "ojvtpuvg"
#input = "abc"
outputLength = 0
hashCounter = 0
fiveZeros = "00000"
output = ""

while (outputLength < 8):
    key = input + str(hashCounter)
    myHash = hashlib.md5(key.encode('utf-8')).hexdigest()
    if (myHash.startswith(fiveZeros)):
        output += myHash[5]
        outputLength += 1
        print ("Output ", output)
    hashCounter += 1

print ("Final output ", output)
