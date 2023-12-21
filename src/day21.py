from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 21

def get_neighbors(x, y, cols, rows, rocks):
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = [(x + d[0], y + d[1]) for d in deltas if 0 <= x + d[0] < cols and 0 <= y + d[1] < rows]
    neighbors = [(x1, y1) for x1, y1 in neighbors if (x1, y1) not in rocks]
    return neighbors


def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    rows = len(data)
    cols = len(data[0])
    rocks = set()
    positions = set()
    for y in range(rows):
        for x in range(cols):
            c = data[y][x]
            if c == "#":
                rocks.add((x, y))
            elif c == "S":
                positions.add((x, y))

    iterations = 64
    for _ in range(iterations):
        new_positions = set()
        for x, y in positions:
            neighbors = get_neighbors(x, y, cols, rows, rocks)
            new_positions.update(neighbors)
        positions = new_positions
    ans = len(positions)
    print(ans)


def get_neighbors2(x, y, cols, rows, rocks):
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = [(x + d[0], y + d[1]) for d in deltas]
    neighbors = [(x1, y1) for x1, y1 in neighbors if (x1 % cols, y1 % rows) not in rocks]
    return neighbors


def task2():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    rows = len(data)
    cols = len(data[0])
    rocks = set()
    positions = set()
    for y in range(rows):
        for x in range(cols):
            c = data[y][x]
            if c == "#":
                rocks.add((x, y))
            elif c == "S":
                positions.add((x, y))

    iterations = 65 + rows * 2
    l = []
    for i in range(iterations):
        new_positions = set()
        for x, y in positions:
            neighbors = get_neighbors2(x, y, cols, rows, rocks)
            new_positions.update(neighbors)
        positions = new_positions
        if (i + 1) % rows == 65:
            l.append(len(positions))
    total_iterations = 26501365
    cycles = total_iterations // rows
    ans = 14716 * (cycles) ** 2 + 14835 * cycles + 3734
    print(ans)

task1()
task2()
