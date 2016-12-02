#!/usr/bin/python3
# Advent of Code
# Day 2 - Part 1
from enum import Enum
class Direction (Enum):
    up = 'U'
    down = 'D'
    left = 'L'
    right = 'R'

class Keypad ():
    def __init__ (self):
        self.keys = [[1,2,3],[4,5,6],[7,8,9]]
        self.position = [1,1]
    
    def isMovable(self, direction):
        if ((self.position[1] == 0) and (direction == Direction.up.value)):
            return False
        if ((self.position[1] == 2) and (direction == Direction.down.value)):
            return False
        if ((self.position[0] == 0) and (direction == Direction.left.value)):
            return False
        if ((self.position[0] == 2) and (direction == Direction.right.value)):
            return False
        return True

    def move(self, direction):
        if (self.isMovable(direction)):
            if (Direction.up.value == direction):
                self.position[1] -= 1
            elif (Direction.down.value == direction):
                self.position[1] += 1
            elif (Direction.left.value == direction):
                self.position[0] -= 1
            elif (Direction.right.value == direction):
                self.position[0] += 1

    def getCode(self):
        positionCoded = str(self.position[0]) + str(self.position[1])
        keypadCode = {'01':1, '10':2, '20':3,
                      '01':4, '11':5, '21':6,
                      '02':7, '12':8, '22':9}
        return keypadCode.get(positionCoded)
        
fo = open("input.txt", "r+")

keypad = Keypad()

for line in fo:
    for char in line: 
        Keypad.move(keypad, char)
    print ("Keypad code: ", Keypad.getCode(keypad))
