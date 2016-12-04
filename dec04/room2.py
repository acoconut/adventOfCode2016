#!/usr/bin/python3
# Advent of code
# Day 4 - Part 2
from collections import Counter

alphabet =('a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z')
alphabetLength = 26
# Read and parse input
fo = open("input.txt", "r+")


for line in fo:
    roomName = ""
    frequency = {}
    room = line.split('-')
    sectorId, checksum = room[-1].split('[')
    
    for code in room[:-1]:
        letters = list(code)
        for letter in letters:
            roomName += alphabet[(alphabet.index(letter)+int(sectorId))%alphabetLength]
        roomName += " "
    if ("northpole" in roomName):
        print (roomName, sectorId)
