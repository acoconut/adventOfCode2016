from enum import Enum
class Direction (Enum):
    up = 'U'
    down = 'D'
    left = 'L'
    right = 'R'

class Keypad ():
    def __init__ (self):
        #self.keys = [[1], [2,3,4], [5,6,7,8,9], [A,B,C], [D]]
        self.position = [0,2]
    
    def isMovable(self, nextPosition):
        goodPositions = [(2,0),
                         (1,1),(2,1),(3,1),
                         (0,2),(1,2),(2,2),(3,2),(4,2),
                         (1,3),(2,3),(3,3),
                         (2,4)]
        if (nextPosition in goodPositions):
            return True
        return False

    def move(self, direction):
        if (Direction.up.value == direction):
            yCoordinate = self.position[1] - 1
            if (self.isMovable((self.position[0], yCoordinate))):
                self.position[1] = yCoordinate
        elif (Direction.down.value == direction):
            yCoordinate = self.position[1] + 1
            if (self.isMovable((self.position[0], yCoordinate))):
                self.position[1] = yCoordinate
        elif (Direction.left.value == direction):
            xCoordinate = self.position[0] - 1
            if (self.isMovable((xCoordinate, self.position[1]))):
                self.position[0] = xCoordinate
        elif (Direction.right.value == direction):
            xCoordinate = self.position[0] + 1
            if (self.isMovable((xCoordinate, self.position[1]))):
                self.position[0] = xCoordinate

    def getCode(self):
        positionCoded = str(self.position[0]) + str(self.position[1])
        keypadCode = {'20':1,
                      '11':2, '21':3, '31':4,
                      '02':5, '12':6, '22':7, '32':8, '42':9,
                      '13':'A', '23':'B', '33':'C',
                      '24':'D'}
        return keypadCode.get(positionCoded)
        

# Read and parse input
fo = open("input.txt", "r+")

keypad = Keypad()

for line in fo:
    for char in line: 
        Keypad.move(keypad, char)
    print ("Keypad code: ", Keypad.getCode(keypad))

#add move method, move should call is movable
