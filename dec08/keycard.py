#!/usr/bin/python3
# Advent of Code
# Day 8 - Part 1 & 2
from enum import Enum
from collections import deque
import re

class Instruction (Enum):
    rect = "rect"
    rotCol = "rotate column"
    rotRow = "rotate row"

class State (Enum):
    on = '#'
    off = '.'

class Keycard ():
    def __init__ (self):
        self.pixelsWide = 50
        self.pixelsTall = 6
        self.keycard = [['.' for _ in range(self.pixelsWide)] for _ in range(self.pixelsTall)]
        
    def rect(self, a, b):
        for row in range(int(b)):
            for col in range(int(a)):
                self.keycard[row][col] = State.on.value

    def rotateCol(self, col, shifts):
        # Get original column
        originalColumn = []
        for i in range(self.pixelsTall):
            originalColumn.append(self.keycard[i][int(col)])

        # Shift
        items = deque(originalColumn)
        items.rotate(int(shifts))
        modifiedColumn = list(items)

        # Put column back
        for i in range(self.pixelsTall):
            self.keycard[i][int(col)] = modifiedColumn[i]
    
    def rotateRow(self, row, shifts):
        items = deque(self.keycard[int(row)])
        items.rotate(int(shifts))
        self.keycard[int(row)] = list(items)

    def printGrid(self):
        for row in self.keycard:
            print (''.join(row))
        print ("\n")

    def countSwitches(self):
        cont = 0
        for row in self.keycard:
            cont += row.count(State.on.value)
        return cont

def parseInstruction(keycard, line):
    (a,b) = re.findall(".*?(\d+).*?", line)
    if (line.startswith(Instruction.rect.value)):
        print ("Instruction: ", line, end="")
        Keycard.rect(keycard, a, b)
        Keycard.printGrid(keycard)
    elif (line.startswith(Instruction.rotCol.value)):
        print ("Instruction: ", line, end="")
        Keycard.rotateCol(keycard, a, b)
        Keycard.printGrid(keycard)
    elif (line.startswith(Instruction.rotRow.value)):
        print ("Instruction: ", line, end="")
        Keycard.rotateRow(keycard, a, b)
        Keycard.printGrid(keycard)
        
fo = open("input.txt", "r+")

keycard = Keycard()

for line in fo:
    parseInstruction(keycard, line)

print ("\nSwitches on", Keycard.countSwitches(keycard))
