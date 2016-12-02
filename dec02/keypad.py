from enum import Enum
class Direction (Enum):
    up = 'U'
    down = 'D'
    left = 'L'
    right = 'R'

class Keypad ():
    def __init__ (self):
        self.keys = [[1,2,3],[4,5,6],[7,8,9]]
        self.position = (1,1)
    
    def isMovable(self, direction):
        if ((self.position[0] == 0) and (self.direction == Direction.up.value)):
            return False
        if ((self.position[0] == 2) and (self.direction == Direction.down.value)):
            return False
        if ((self.position[1] == 0) and (self.direction == Direction.left.value)):
            return False
        if ((self.position[1] == 2) and (self.direction == Direction.right.value)):
            return False
        return True

    #def move(self, direction, distance):
        

# Read and parse input
fo = open("input.txt", "r+")

keypad = Keypad()

for line in fo:
    for char in line: 
        Keypad.isMovable(keypad, char)

#add move method, move should call is movable
