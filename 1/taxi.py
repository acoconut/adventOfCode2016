from enum import Enum
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

    def move (self, turn, distance):
        if (self.looking == Cardinal.north):
            if (Direction.right.value == turn):
                self.east = self.east + int(distance)
                self.looking = Cardinal.east;
            elif (Direction.left.value == turn):
                self.east = self.east - int(distance)
                self.looking = Cardinal.west;
        elif (self.looking == Cardinal.east):
            if (Direction.right.value == turn):
                self.north = self.north - int(distance)
                self.looking = Cardinal.south;
            elif (Direction.left.value == turn):
                self.north = self.north + int(distance)
                self.looking = Cardinal.north;
        elif (self.looking == Cardinal.south):
            if (Direction.right.value == turn):
                self.east = self.east - int(distance)
                self.looking = Cardinal.west;
            elif (Direction.left.value == turn):
                self.east = self.east + int(distance)
                self.looking = Cardinal.east;
        elif (self.looking == Cardinal.west):
            if (Direction.right.value == turn):
                self.north = self.north + int(distance)
                self.looking = Cardinal.north;
            elif (Direction.left.value == turn):
                self.north = self.north - int(distance)
                self.looking = Cardinal.south;

    def printCoordinates(self):
        print ("North: ", self.north)
        print ("East: ", self.east)

    def printBlocksAway(self):
        print (abs(self.north) + abs(self.east))

fo = open("input.txt", "r+")
input = fo.read()

directions = input.replace(" ", "").strip().split(',')
taxi = Taxi()
for direction in directions:
    print ("Direction ", direction[0])
    print ("Distance ", direction[1:])
    Taxi.move(taxi, direction[0], direction[1:])

Taxi.printCoordinates(taxi)
Taxi.printBlocksAway(taxi)
