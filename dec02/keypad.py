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

