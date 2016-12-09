#!/usr/bin/python3
# Advent of code
# Day 9 - Part 1
import re
from math import floor

def parseBracket(content):
    (a, b) = re.findall(".*?(\d+).*?", content)
    return (a, b)

fo = open("input.txt", "r+")
inputFile = fo.read()
input = list(inputFile)
while (' ' in input):
    input.remove(' ')
output = list()

treatingBracket = False
outputIndex = 0 

openBracket = '('
closeBracket = ')'
inputIndex = 0

while (inputIndex < len(input)):
    if ((input[inputIndex] == openBracket) and (not treatingBracket)):
        closeBracketIndex = input[inputIndex:].index(closeBracket)+inputIndex
        (chars, times) = parseBracket(inputFile[inputIndex+1:closeBracketIndex])
        inputIndex = closeBracketIndex + 1 + int(chars)
        charsToRepeat = input[closeBracketIndex+1:closeBracketIndex+1+int(chars)]
        charsToRepeat.reverse()
        for i in range(int(times)):
            [output.insert(outputIndex, x) for x in charsToRepeat]
            outputIndex += int(chars)
    else:
        output.append(input[inputIndex])
        inputIndex += 1
        outputIndex +=1
        
print ("Length ", len(output))
