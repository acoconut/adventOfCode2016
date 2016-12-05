#!/usr/bin/python3
# Advent of code
# Day 5 - Part 2
import hashlib

input = "ojvtpuvg"
#input = "abc"
hashCounter = 0
fiveZeros = "00000"
notKnownChar = '_'
output = [notKnownChar] * 8

while (notKnownChar in output):
    key = input + str(hashCounter)
    myHash = hashlib.md5(key.encode('utf-8')).hexdigest()
    index = myHash[5]
    if (myHash.startswith(fiveZeros) and index.isnumeric() and int(index) < 8 and output[int(index)] == notKnownChar):
        output[int(index)] = myHash[6]
        print ("Output ", output)
    hashCounter += 1

print ("Final output ", ''.join(output))
