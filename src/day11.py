from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 11


def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    data = [list(line) for line in data]
    new_data = []
    for line in data:
        new_data.append(line)
        if "#" not in line:
            new_data.append(line.copy())
    data = new_data
    new_cols = []
    for x in range(len(data[0])):
        s = ""
        for y in range(len(data)):
            s += data[y][x]
        if "#" not in s:
            new_cols.append(x)
    for y in range(len(data)):
        for x in new_cols:
            data[y].insert(x + new_cols.index(x), ".")
    galaxies = set()
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "#":
                galaxies.add((x, y))
    distances = {}
    for g1 in galaxies:
        for g2 in galaxies:
            if g1 != g2:
                d = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
                if (g2, g1) not in distances:
                    distances[(g1, g2)] = d
    ans = sum(distances.values())
    print(ans)


def task2():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    data = [list(line) for line in data]
    scale = 1000000
    new_rows = []
    for y in range(len(data)):
        line = data[y]
        if "#" not in line:
            new_rows.append(y)

    new_cols = []
    for x in range(len(data[0])):
        s = ""
        for y in range(len(data)):
            s += data[y][x]
        if "#" not in s:
            new_cols.append(x)

    galaxies = set()
    for y in range(len(data)):
        y_expanded_count = len([e for e in new_rows if y > e])
        for x in range(len(data[y])):
            x_expanded_count = len([e for e in new_cols if x > e])
            if data[y][x] == "#":
                galaxies.add((x + x_expanded_count * (scale - 1), y + y_expanded_count * (scale - 1)))

    distances = {}
    for g1 in galaxies:
        for g2 in galaxies:
            if g1 != g2:
                d = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
                if (g2, g1) not in distances:
                    distances[(g1, g2)] = d
    ans = sum(distances.values())
    print(ans)


task1()
task2()
