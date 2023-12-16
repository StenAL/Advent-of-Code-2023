from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 16

def get_neighbors(pos, rows, cols, objects):
    x, y, direction = pos
    neighbors = []
    left = (x - 1, y)
    right = (x + 1, y)
    up = (x, y - 1)
    down = (x, y + 1)
    directions = ["u", "r", "d", "l"]
    dir_to_square = {"u": up, "r": right, "d": down, "l": left}
    if (x,y) in objects:
        o = objects[(x,y)]
        if o == "/":
            if direction in ["r", "l"]:
                new_direction = directions[(directions.index(direction) - 1) % len(directions)]
                neighbors.append((*dir_to_square[new_direction], new_direction))
            else:
                new_direction = directions[(directions.index(direction) + 1) % len(directions)]
                neighbors.append((*dir_to_square[new_direction], new_direction))
        elif o == "\\":
            if direction in ["r", "l"]:
                new_direction = directions[(directions.index(direction) + 1) % len(directions)]
                neighbors.append((*dir_to_square[new_direction], new_direction))
            else:
                new_direction = directions[(directions.index(direction) - 1) % len(directions)]
                neighbors.append((*dir_to_square[new_direction], new_direction))
        elif o == "|":
            if direction in ["l", "r"]:
                neighbors.append((*up, "u"))
                neighbors.append((*down, "d"))
            else:
                neighbors.append((*up, "u") if direction == "u" else (*down, "d"))
        elif o == "-":
            if direction in ["u", "d"]:
                neighbors.append((*left, "l"))
                neighbors.append((*right, "r"))
            else:
                neighbors.append((*left, "l") if direction == "l" else (*right, "r"))
    else:
        neighbors.append((*dir_to_square[direction], direction))
    neighbors = [n for n in neighbors if 0 <= n[0] < cols and 0 <= n[1] < rows ]
    return neighbors


def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    rows = len(data)
    cols = len(data[0])
    objects = {}
    for y in range(rows):
        for x in range(cols):
            c = data[y][x]
            if c != ".":
                objects[(x, y)] = c
    seen = set()
    current_positions = { (0, 0, "r") }
    while len(current_positions) > 0:
        pos = current_positions.pop()
        seen.add(pos)
        neighbors = [n for n in get_neighbors(pos, rows, cols, objects) if n not in seen]
        current_positions.update(neighbors)
    energized = { (p[0], p[1]) for p in seen }
    ans = len(energized)
    print(ans)


def task2():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    rows = len(data)
    cols = len(data[0])
    objects = {}
    edges = []
    for y in range(rows):
        for x in range(cols):
            c = data[y][x]
            if c != ".":
                objects[(x, y)] = c
            if x == 0:
                edges.append((x, y, "r"))
            if y == 0:
                edges.append((x, y, "d"))
            if x == cols - 1:
                edges.append((x, y, "l"))
            if y == rows - 1:
                edges.append((x, y, "u"))

    energized_counts = []
    for edge in edges:
        seen = set()
        current_positions = { edge }
        while len(current_positions) > 0:
            pos = current_positions.pop()
            seen.add(pos)
            neighbors = [n for n in get_neighbors(pos, rows, cols, objects) if n not in seen]
            current_positions.update(neighbors)
        energized = { (p[0], p[1]) for p in seen }
        energized_counts.append(len(energized))
    ans = max(energized_counts)
    print(ans)


task1()
task2()
