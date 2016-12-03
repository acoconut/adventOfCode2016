#!/usr/bin/python3
# Advent of code
# Day 3 - Part 1
def isTriangle(a, b, c):
    return ((a + b) > c)

fo = open("input.txt", "r+")

cont = 0
for line in fo:
    sides = line.strip().split()
    sides.sort(key = int)
    if (isTriangle(int(sides[0]), int(sides[1]), int(sides[2]))):
        cont += 1
        
print ("Triangles: ", cont)
