#!/usr/bin/python3
# Advent of code
# Day 3 - Part 1
def isTriangle(a, b, c):
    side = [int(a),int(b),int(c)]
    side.sort()
    return ((side[0] + side[1]) > side[2])

def countTriangles(sides):
    triangles = 0
    if (isTriangle(sides[0][0], sides[1][0], sides[2][0])):
        triangles += 1
    if (isTriangle(sides[0][1], sides[1][1], sides[2][1])):
        triangles += 1
    if (isTriangle(sides[0][2], sides[1][2], sides[2][2])):
        triangles += 1
    return triangles

fo = open("input.txt", "r+")


contLines = 1
cont = 0
sides = list()

for line in fo:
    if (not (contLines % 3 == 0)):
        sides.append(line.strip().split())
        contLines += 1
    else:
        sides.append(line.strip().split())
        cont += countTriangles(sides)
        contLines = 1
        sides.clear()
        
        
print ("Triangles: ", cont)
