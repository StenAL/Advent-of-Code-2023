from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 18

def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    dug = set()
    last_dug = None
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    for line in data:
        direction, distance, color = line.split()
        d = directions[direction]
        if last_dug is None:
            last_dug = (-d[0], -d[1])
        distance = int(distance)
        for i in range(distance):
            p = (last_dug[0] + d[0], last_dug[1] + d[1])
            last_dug = p
            dug.add(p)
    top_left = min(dug)
    q = [(top_left[0] + 1, top_left[1] + 1)]
    while len(q) > 0:
        p = q.pop()
        for d in directions.values():
            neighbor = (p[0] + d[0], p[1] + d[1])
            if neighbor not in dug:
                q.append(neighbor)
                dug.add(neighbor)
    ans = len(dug)
    print(ans)


def task2():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    dug = set()
    last_dug = (0, 0)
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    color_to_direction = { 0: "R", 1: "D", 2: "L", 3: "U"}
    vertices = []
    circumference = 0
    for line in data:
        _, _, color = line.split()
        color = color.strip("(").strip(")").strip("#")
        distance = int(color[:-1], 16)
        direction = color_to_direction[int(color[-1])]
        #direction, distance, color = line.split()
        d = directions[direction]
        distance = int(distance)
        end = (last_dug[0] + d[0] * distance, last_dug[1] + d[1] * distance)
        circumference += distance
        dug.add((last_dug, end))
        vertices.append(end)
        last_dug = end
    vertices.insert(0, vertices[-1])
    ans = int(area(vertices) + circumference / 2 + 1)
    print(ans)

def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in segments(p)))

def segments(p):
    return zip(p, p[1:] + [p[0]])

task1()
task2()

