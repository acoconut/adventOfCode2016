#!/usr/bin/python3
# Advent of code
# Day 1 - Part 2
from enum import Enum
import sys
class Cardinal(Enum):
    north = 'N'
    east = 'E' 
    west = 'W'
    south = 'S'

class Direction(Enum):
    right = 'R' 
    left = 'L'

class Taxi:
    def __init__(self):
        self.north = 0
        self.east = 0 
        self.looking = Cardinal.north
        self.seenCoordinates = [(0,0)]

    def addSeenCoordinates(self):
        coordinate = (self.east, self.north)
        if (coordinate not in self.seenCoordinates):
            self.seenCoordinates.append((self.east, self.north))
        else:
            print ("Coordinate seen twice! ", coordinate)
            print ("Solution: ", self.getBlocksAway())
            sys.exit()
            
    def move (self, turn, distance):
        if (self.looking == Cardinal.north):
            if (Direction.right.value == turn):
                for i in range (int(distance)):   
                    self.east = self.east + 1
                    self.addSeenCoordinates()
                self.looking = Cardinal.east;
            elif (Direction.left.value == turn):
                for i in range (int(distance)):   
                    self.east = self.east - 1
                    self.addSeenCoordinates()
                self.looking = Cardinal.west;
        elif (self.looking == Cardinal.east):
            if (Direction.right.value == turn):
                for i in range (int(distance)):   
                    self.north = self.north - 1
                    self.addSeenCoordinates()
                self.looking = Cardinal.south
            elif (Direction.left.value == turn):
                for i in range (int(distance)):   
                    self.north = self.north + 1
                    self.addSeenCoordinates()
                self.looking = Cardinal.north
        elif (self.looking == Cardinal.south):
            if (Direction.right.value == turn):
                for i in range (int(distance)):   
                    self.east = self.east - 1
                    self.addSeenCoordinates()
                self.looking = Cardinal.west;
            elif (Direction.left.value == turn):
                for i in range (int(distance)):   
                    self.east = self.east + 1
                    self.addSeenCoordinates()
                self.looking = Cardinal.east;
        elif (self.looking == Cardinal.west):
            if (Direction.right.value == turn):
                for i in range (int(distance)):
                    self.north = self.north + 1
                    self.addSeenCoordinates()
                self.looking = Cardinal.north;
            elif (Direction.left.value == turn):
                for i in range (int(distance)):   
                    self.north = self.north - 1
                    self.addSeenCoordinates()
                self.looking = Cardinal.south     

    def getBlocksAway(self):
        return (abs(self.north) + abs(self.east))

# Read and parse input
fo = open("input.txt", "r+")
input = fo.read()
directions = input.replace(" ", "").strip().split(',')

# Let's get started
taxi = Taxi()
for direction in directions:
    Taxi.move(taxi, direction[0], direction[1:])
