#!/usr/bin/python3
# Advent of code
# Day 9 - Part 2
from itertools import takewhile, islice

def parseBracket(content):
    (a, b) = re.findall(".*?(\d+).*?", content)
    return (a, b)

fo = open("input.txt", "r+")
input = fo.read()

openBracket = '('
discardChars = 'x)'

def decompress(input):
    output = 0
    characters = iter(input)
    for character in characters:
        if (character == openBracket):
            char, times = map(int, [''.join(takewhile(lambda i: i not in discardChars, characters)) for _ in (0, 1)])
            rest = ''.join(islice(characters, char))
            output += (decompress(rest))*times
        else:
            output += 1
    return output

print ("Length ", decompress(input))
