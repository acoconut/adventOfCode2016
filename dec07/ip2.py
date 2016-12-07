#!/usr/bin/python3
# Advent of code
# Day 7 - Part 2
import re

def isABA(possibleABA):
    if (possibleABA[0] == possibleABA[1]):
        return False
    if (possibleABA[0] == possibleABA[-1]):
        return True
    else:
        return False

def findABA(line):
    listOfABA = []
    length = len(line)-2
    if (length < 1):
        return listOfABA
    for i in range(length):
        if (isABA(line[i:i+3])):
            listOfABA.append(line[i:i+3])
    return listOfABA

def parseInput(line):
    hypernet = re.findall(r'\[.+?\]', line)    
    supernet = re.findall(r'([^[\]]+)(?:$|\[)', line)
    supernet[-1] = supernet[-1][:-1]
    return (hypernet, supernet)

def createBAB(ABA):
    return ABA[1] + ABA[0] + ABA[1]

fo = open("input.txt", "r+")
input = fo.readlines()

cont = 0
for line in input:
    (hypernet, supernet) = parseInput(line)
    supernetABAs = []
    supernetBABs = []
    hypernetBABs = []
    for i in supernet:
        supernetABAs += findABA(i)
    for i in supernetABAs:
        supernetBABs.append(createBAB(i))
    for i in hypernet:
        hypernetBABs += findABA(i)

    if (set(supernetBABs).intersection(hypernetBABs)):
        cont += 1

print ("Total ", cont)
