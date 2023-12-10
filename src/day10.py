from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 10


def get_neighbors(x, y, x_max, y_max):
    neighbors = {}
    if 0 <= x - 1:
        neighbors["left"] = (x - 1, y)
    if x + 1 <= x_max:
        neighbors["right"] = (x + 1, y)
    if 0 <= y - 1:
        neighbors["up"] = (x, y - 1)
    if y + 1 <= y_max:
        neighbors["down"] = (x, y + 1)
    return neighbors


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test2")
    points = {}
    start = (0, 0)
    rows = len(data)
    cols = len(data[0])
    for y in range(rows):
        for x in range(cols):
            c = data[y][x]
            if c != ".":
                points[(x, y)] = c
                if c == "S":
                    start = (x, y)
    loop = {start: 0}
    q = [(start, 0)]
    left_valid = ["-", "F", "L"]
    right_valid = ["-", "J", "7"]
    up_valid = ["|", "7", "F"]
    down_valid = ["|", "J", "L"]
    while len(q) > 0:
        (x, y), d = q.pop(0)
        neighbors = get_neighbors(x, y, rows - 1, cols - 1)
        if "left" in neighbors and neighbors["left"] in points and points[neighbors["left"]] in left_valid:
            l = neighbors["left"]
            if l not in loop:
                loop[l] = d + 1
                q.append((l, d + 1))
        if "right" in neighbors and neighbors["right"] in points and points[neighbors["right"]] in right_valid:
            l = neighbors["right"]
            if l not in loop:
                loop[l] = d + 1
                q.append((l, d + 1))
        if "up" in neighbors and neighbors["up"] in points and points[neighbors["up"]] in up_valid:
            l = neighbors["up"]
            if l not in loop:
                loop[l] = d + 1
                q.append((l, d + 1))
        if "down" in neighbors and neighbors["down"] in points and points[neighbors["down"]] in down_valid:
            l = neighbors["down"]
            if l not in loop:
                loop[l] = d + 1
                q.append((l, d + 1))
    ans = max(loop.values())
    print(ans)

def pretty_print(rows, cols, loop, points):
    for y in range(rows):
        for x in range(cols):
            if (x, y) in loop:
                v = points[(x,y)].replace("L", "╰").replace("F", "╭").replace("J", "╯").replace("7", "╮")
                print(v, end="")
            else:
                print(" ", end="")
        print()

def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test2")
    points = {}
    start = (0, 0)
    rows = len(data)
    cols = len(data[0])
    for y in range(rows):
        for x in range(cols):
            c = data[y][x]
            if c != ".":
                points[(x, y)] = c
            if c == "S":
                start = (x, y)
    loop = {start: 0}
    q = [(start, 0)]
    left_valid = ["-", "F", "L", "S"]
    right_valid = ["-", "J", "7", "S"]
    up_valid = ["|", "7", "F", "S"]
    down_valid = ["|", "J", "L", "S"]
    while len(q) > 0:
        (x, y), d = q.pop(0)
        v = points[(x, y)]
        neighbors = get_neighbors(x, y, cols - 1, rows - 1)
        left, right, up, down = False, False, False, False
        if "left" in neighbors and neighbors["left"] in points and points[neighbors["left"]] in left_valid and v in right_valid:
            left = True
            l = neighbors["left"]
            if l not in loop:
                loop[l] = d + 1
                q.append((l, d + 1))
        if "right" in neighbors and neighbors["right"] in points and points[neighbors["right"]] in right_valid and v in left_valid:
            right = True
            l = neighbors["right"]
            if l not in loop:
                loop[l] = d + 1
                q.append((l, d + 1))
        if "up" in neighbors and neighbors["up"] in points and points[neighbors["up"]] in up_valid and v in down_valid:
            up = True
            l = neighbors["up"]
            if l not in loop:
                loop[l] = d + 1
                q.append((l, d + 1))
        if "down" in neighbors and neighbors["down"] in points and points[neighbors["down"]] in down_valid and v in up_valid:
            down = True
            l = neighbors["down"]
            if l not in loop:
                loop[l] = d + 1
                q.append((l, d + 1))
        if v == "S":
            if left and right:
                points[(x, y)] = "-"
            if up and down:
                points[(x, y)] = "|"
            if left and up:
                points[(x, y)] = "J"
            if left and down:
                points[(x, y)] = "7"
            if right and up:
                points[(x, y)] = "L"
            if right and down:
                points[(x, y)] = "F"

    # pretty_print(rows, cols, loop, points)
    for y in range(rows):
        for x in range(cols):
            if (x, y) not in loop:
                points[(x, y)] = "."

    ans = 0
    for y in range(rows):
        cross_count = 0
        for x in range(cols):
            c = points[(x, y)]
            if c in ["J", "|", "L"]:
                cross_count += 1
            if c == "." and cross_count % 2 == 1:
                ans += 1
    print(ans)

task1()
task2()
