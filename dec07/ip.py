#!/usr/bin/python3
# Advent of code
# Day 7 - Part 1
import re

def isABBA(possibleABBA):
    if (possibleABBA[0] == possibleABBA[1]):
        return False
    if (possibleABBA[:2] == possibleABBA[3:1:-1]):
        return True
    else:
        return False

def checkABBA(line):
    length = len(line)-3
    if (length < 1):
        return False
    for i in range(length):
        if (isABBA(line[i:i+4])):
            return True
    return False

def parseInput(line):
    hypernet = re.findall(r'\[.+?\]', line)    
    supernet = re.findall(r'([^[\]]+)(?:$|\[)', line)
    supernet[-1] = supernet[-1][:-1]
    return (hypernet, supernet)

fo = open("input.txt", "r+")
input = fo.readlines()

cont = 0
for line in input:
    goodHypernet = True
    goodSupernet = False
    (hypernet, supernet) = parseInput(line)
    for i in hypernet:
        if (checkABBA(i[1:-1])):
            goodHypernet = False
    for i in supernet:
        if (checkABBA(i)):
            goodSupernet = True
    if (goodHypernet and goodSupernet):
        cont +=1

print ("Total ", cont)
