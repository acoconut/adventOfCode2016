#!/usr/bin/python3
# Advent of code
# Day 9 - Part 1
import re
from math import floor

def parseBracket(content):
    (a, b) = re.findall(".*?(\d+).*?", content)
    return (a, b)

fo = open("inputtest.txt", "r+")
inputFile = fo.read()
input = list(inputFile)
output = list(input)

openBracket = '('
closeBracket = ')'

openBrackets = [i for i, x in enumerate(input) if x == openBracket]
closeBrackets = [i for i, x in enumerate(input) if x == closeBracket]
print (openBrackets)
print (closeBrackets)

for bracketIndex in range(len(openBrackets)):
    print (inputFile[int(openBrackets[bracketIndex]+1):int(closeBrackets[bracketIndex])])
    (characters, times) = parseBracket(inputFile[int(openBrackets[bracketIndex]+1):int(closeBrackets[bracketIndex])])
    [output.remove(input[x]) for x in range(openBrackets[bracketIndex], closeBrackets[bracketIndex]+1)]
    charactersToRepeatIndex = closeBrackets[bracketIndex]+1
    charactersToRepeat = input[charactersToRepeatIndex:charactersToRepeatIndex+int(characters)]
    print ("CTR ", charactersToRepeat)
    # Check if there are any characters that look like markers and remove them
    cont = 0 
    while (openBracket in charactersToRepeat):
        print ("OB ", openBrackets, bracketIndex)
        charactersToRepeat.remove(openBrackets[bracketIndex+cont])
        print ("OC ", openBrackets)
        cont +=1
    print (charactersToRepeat)
    #[output.insert(bracketIndex,  
