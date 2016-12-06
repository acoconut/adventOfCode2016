#!/usr/bin/python3
# Advent of code
# Day 6 - Part 1
from collections import Counter

fo = open("input.txt", "r+")

lineLength = 8
letters = [[] for _ in range(lineLength)]
for line in fo:
    for i in range(lineLength):
        letters[i].append(line[i])

code = ""
for i in range(lineLength):
    code += str(Counter(letters[i]).most_common(1)[0][0])
print (code)
