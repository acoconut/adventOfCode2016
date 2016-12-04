#!/usr/bin/python3
# Advent of code
# Day 4 - Part 1
from collections import Counter
    
# Read and parse input
fo = open("input.txt", "r+")

sumSectorIds = 0
for line in fo:
    frequency = {}
    room = line.split('-')
    sectorId, checksum = room[-1].split('[')
    if (checksum[-2] == ']'):
        checksum = checksum[:-2]
    else:
        checksum = checksum[:-1]
    for code in room[:-1]:
        letters = list(code)
        for letter in letters:
            frequency[letter] = frequency.get(letter, 0) + 1
    myChecksum = "".join([k for k, v in sorted(Counter(frequency).most_common(), key=lambda e: (-e[1], e[0]))[:5]])
    if (checksum == myChecksum):
        sumSectorIds += int(sectorId)

print ("Sector IDs sum ", sumSectorIds)
