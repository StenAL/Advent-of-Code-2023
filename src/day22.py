from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 22


def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    layers = defaultdict(set) # height -> (x,y)
    coord_to_brick = {}
    bricks = defaultdict(set)
    for i in range(len(data)):
        line = data[i]
        start, end = line.split("~")
        start = [int(e) for e in start.split(",")]
        end = [int(e) for e in end.split(",")]
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                for z in range(start[2], end[2] + 1):
                    brick_id = chr(ord("a") + i)
                    layers[z].add((x, y))
                    coord_to_brick[(x, y, z)] = brick_id
                    bricks[brick_id].add((x, y, z))

    done = False
    while not done:
        done = True
        for brick_id, coords in bricks.items():
            bottom_layer_idx = min(z for _, _, z in coords)
            bottom_layer_cubes = [(x, y) for x, y, z in coords if z == bottom_layer_idx]
            directly_below_bottom = [(x, y) for x, y in layers[bottom_layer_idx - 1] if (x, y) in bottom_layer_cubes]
            if bottom_layer_idx > 1 and len(directly_below_bottom) == 0: # can fall
                top_layer_idx = max(z for _, _, z in coords)
                top_layer_cubes = [(x, y) for x, y, z in coords if z == top_layer_idx]
                for x, y in top_layer_cubes:
                    del coord_to_brick[(x, y, top_layer_idx)]
                    layers[top_layer_idx].discard((x, y))
                    bricks[brick_id].discard((x, y, top_layer_idx))
                    layers[bottom_layer_idx - 1].add((x, y))
                    bricks[brick_id].add((x, y, bottom_layer_idx - 1))
                    coord_to_brick[(x, y, bottom_layer_idx - 1)] = brick_id
                done = False
    bricks_above = defaultdict(set)
    bricks_below = defaultdict(int)
    for brick_id, coords in bricks.items():
        bottom_layer_idx = min(z for _, _, z in coords)
        bottom_layer_cubes = [(x, y) for x, y, z in coords if z == bottom_layer_idx]
        directly_below_bottom = [(x, y) for x, y in layers[bottom_layer_idx - 1] if (x, y) in bottom_layer_cubes]
        for x, y in directly_below_bottom:
            bottom_brick = coord_to_brick[(x, y, bottom_layer_idx - 1)]
            if brick_id not in bricks_above[bottom_brick]:
                bricks_above[bottom_brick].add(brick_id)
                bricks_below[brick_id] += 1
    ans = 0
    for b in bricks:
        if len(bricks_above[b]) == 0:
            ans += 1
        elif all(bricks_below[brick_above] > 1 for brick_above in bricks_above[b]):
            ans += 1
    print(ans) 


def get_falling_bricks(disintegrated, bricks, bricks_below):
    falling = set()
    for b in bricks:
        if len(bricks_below[b]) > 0 and bricks_below[b].intersection(disintegrated) == bricks_below[b] and b not in disintegrated:
            falling.add(b)
            # print(f"{disintegrated} -> fall {b}")
    if len(falling) == 0:
        return len(disintegrated)
    disintegrated.update(falling)
    return get_falling_bricks(disintegrated, bricks, bricks_below)


def task2():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    layers = defaultdict(set) # height -> (x,y)
    coord_to_brick = {}
    bricks = defaultdict(set)
    for i in range(len(data)):
        line = data[i]
        start, end = line.split("~")
        start = [int(e) for e in start.split(",")]
        end = [int(e) for e in end.split(",")]
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                for z in range(start[2], end[2] + 1):
                    brick_id = chr(ord("a") + i)
                    layers[z].add((x, y))
                    coord_to_brick[(x, y, z)] = brick_id
                    bricks[brick_id].add((x, y, z))

    done = False
    while not done:
        done = True
        for brick_id, coords in bricks.items():
            bottom_layer_idx = min(z for _, _, z in coords)
            bottom_layer_cubes = [(x, y) for x, y, z in coords if z == bottom_layer_idx]
            directly_below_bottom = [(x, y) for x, y in layers[bottom_layer_idx - 1] if (x, y) in bottom_layer_cubes]
            if bottom_layer_idx > 1 and len(directly_below_bottom) == 0: # can fall
                top_layer_idx = max(z for _, _, z in coords)
                top_layer_cubes = [(x, y) for x, y, z in coords if z == top_layer_idx]
                for x, y in top_layer_cubes:
                    del coord_to_brick[(x, y, top_layer_idx)]
                    layers[top_layer_idx].discard((x, y))
                    bricks[brick_id].discard((x, y, top_layer_idx))
                    layers[bottom_layer_idx - 1].add((x, y))
                    bricks[brick_id].add((x, y, bottom_layer_idx - 1))
                    coord_to_brick[(x, y, bottom_layer_idx - 1)] = brick_id
                done = False
    bricks_above = defaultdict(set)
    bricks_below = defaultdict(set)
    for brick_id, coords in bricks.items():
        bottom_layer_idx = min(z for _, _, z in coords)
        bottom_layer_cubes = [(x, y) for x, y, z in coords if z == bottom_layer_idx]
        directly_below_bottom = [(x, y) for x, y in layers[bottom_layer_idx - 1] if (x, y) in bottom_layer_cubes]
        for x, y in directly_below_bottom:
            bottom_brick = coord_to_brick[(x, y, bottom_layer_idx - 1)]
            if brick_id not in bricks_above[bottom_brick]:
                bricks_above[bottom_brick].add(brick_id)
                bricks_below[brick_id].add(bottom_brick)
    ans = 0
    for b in bricks:
        s = { b }
        x = get_falling_bricks(s, bricks, bricks_below)
        falling_count = len(s - { b })
        ans += falling_count
        # print(b, falling_count)
    print(ans)


task1()
task2()

