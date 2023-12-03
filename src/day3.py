from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 3

def get_neighbors(x, y, x_max, y_max):
    neighbors = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            n_x = x + dx
            n_y = y + dy
            if 0 <= n_x <= x_max and 0 <= n_y <= y_max:
                neighbors.append((x + dx, y + dy))
    # print((x, y), neighbors)
    return neighbors

def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test2")
    parts = []
    rows = len(data)
    cols = len(data[0])
    for y in range(rows):
        acc = ""
        is_part = False
        for x in range(cols):
            c = data[y][x]
            if c.isnumeric():
                acc += c
            if acc.isnumeric() and c.isnumeric():
                neighbors = get_neighbors(x, y, cols - 1, rows - 1)
                neighbor_values = [data[ny][nx] for nx, ny in neighbors]
                is_part = is_part or any(n != "." and not n.isnumeric() for n in neighbor_values)

            if not c.isnumeric() or x == cols - 1:
                if is_part:
                    parts.append(int(acc))
                acc = ""
                is_part = False
    ans = sum(parts)
    print(ans)


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    rows = len(data)
    cols = len(data[0])
    ratios = defaultdict(list)
    for y in range(rows):
        acc = ""
        gears = set()
        for x in range(cols):
            c = data[y][x]
            if c.isnumeric():
                acc += c
            if acc.isnumeric() and c.isnumeric():
                neighbors = get_neighbors(x, y, cols - 1, rows - 1)
                gears.update((nx, ny) for nx, ny in neighbors if data[ny][nx] == "*")

            if not c.isnumeric() or x == cols - 1:
                if acc.isnumeric():
                    for g in gears:
                        ratios[g].append(int(acc))
                acc = ""
                gears = set()
    valid_gears = [(k, v) for k, v in ratios.items() if len(v) == 2]
    print(valid_gears)
    ans = sum(prod(v) for k, v in valid_gears)
    print(ans)


# task1()
task2()
