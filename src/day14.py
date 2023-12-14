from util import *
import re
from collections import *
import copy
from functools import reduce
from math import prod

day = 14


def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    rows = len(data)
    cols = len(data[0])
    clusters = []
    for x in range(cols):
        last_square = -1
        round_count = 0
        for y in range(rows):
            c = data[y][x]
            if c == "#":
                clusters.append((last_square, round_count))
                last_square = y
                round_count = 0
            elif c == "O":
                round_count += 1
        clusters.append((last_square, round_count))
    ans = 0
    for (square_idx, round_count) in clusters:
        load_start = rows - square_idx
        load_end = load_start - round_count
        ans += sum(range(load_end, load_start))
    print(ans)

def roll(rocks):
    new_rocks = defaultdict(list)
    clusters = []
    for x, rocks in rocks.items():
        last_square = -1
        round_count = 0
        for rock_type, y in rocks:
            if rock_type == "#":
                new_rocks[x].append(("#", y))
                clusters.append((x, last_square, round_count))
                last_square = y
                round_count = 0
            else:
                round_count += 1
        clusters.append((x, last_square, round_count))

    for (x, square_idx, round_count) in clusters:
        for i in range(round_count):
            new_rocks[x].append(("O", square_idx + 1 + i))
    for v in new_rocks.values():
        v.sort(key=lambda e: e[1])
    return new_rocks

def get_load(rocks, rows):
    load = 0
    for rock_list in rocks.values():
        for rock_type, y in rock_list:
            if rock_type == "O":
                load += rows - y
    return load

def rotate_right(rocks, rows):
    new_rocks = defaultdict(list)
    for x, rock_list in rocks.items():
        for rock_type, y in rock_list:
            new_x = rows - 1 - y
            new_y = x
            new_rocks[new_x].append((rock_type, new_y))
    for v in new_rocks.values():
        v.sort(key=lambda e: e[1])
    return new_rocks


def task2():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    rows = len(data)
    cols = len(data[0])
    rocks = defaultdict(list) # column -> rocks
    for x in range(cols):
        for y in range(rows):
            c = data[y][x]
            if c == "#":
                rocks[x].append(("#", y))
            elif c == "O":
                rocks[x].append(("O", y))
    loads = []
    load_to_cycle = defaultdict(list)
    cycles = 500
    for j in range(cycles):
        for i in range(4):
            rocks = roll(rocks)
            row_count = rows if i % 2 == 0 else cols
            rocks = rotate_right(rocks, row_count)
        load = get_load(rocks, rows)
        load_to_cycle[load].append(j)
        loads.append(load)
    #d = { k: v for k,v in load_to_cycle.items() if len(v) > 10 }
    cycle_length = 21 # from inspecting d above
    cycle = loads[400:400 + cycle_length]
    ans = cycle[(1000000000 - 400) % cycle_length - 1]
    print(ans)


task1()
task2()
