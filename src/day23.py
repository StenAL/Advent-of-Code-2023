from util import *
from collections import *
import copy
from functools import reduce
from math import prod
import heapq

day = 23

def get_neighbors(x, y, points):
    if points[(x, y)] != ".":
        slope_to_delta = { ">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}
        d = slope_to_delta[points[(x, y)]]
        return [(x + d[0], y + d[1])]
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = [(x + d[0], y + d[1]) for d in deltas if (x + d[0], y + d[1]) in points]
    return neighbors


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    rows = len(data)
    cols = len(data[0])
    points = {}
    for y in range(rows):
        for x in range(cols):
            c = data[y][x]
            if c != "#":
                points[(x, y)] = c
    q = [(1, 0, 0, set())]
    best = {(1, 0): 0}
    while len(q) > 0:
        x, y, d, seen = q.pop(0)
        if (x, y) in best and d < best[(x, y)]:
            continue
        neighbors = [n for n in get_neighbors(x, y, points) if n not in seen]
        for nx, ny in neighbors:
            q.append((nx, ny, d + 1, seen.union([(x, y)])))
            best[(nx, ny)] = d + 1
    ans = best[(cols - 2, rows - 1)]
    print(ans)


def get_neighbors2(p, points):
    x, y = p
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = [(x + d[0], y + d[1]) for d in deltas]
    neighbors = [n for n in neighbors if n in points]
    return neighbors

def get_next_intersection(p, next_point, points):
    seen = {p}
    neighbors = [neighbor for neighbor in get_neighbors2(next_point, points) if neighbor not in seen]
    distance = 1
    while len(neighbors) == 1:
        distance += 1
        seen.add(next_point)
        [next_point] = neighbors
        neighbors = [neighbor for neighbor in get_neighbors2(next_point, points) if neighbor not in seen]
    return next_point, distance

def path_to_end_exists(p, end, neighbors, seen):
    q = [p]
    reachable = set()
    while len(q) > 0:
        p = q.pop(0)
        reachable.add(p)
        valid_neighbors = [n for n in neighbors[p] if n not in seen and n not in reachable]
        for n in valid_neighbors:
            q.append(n)
    return end in reachable
def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    rows = len(data)
    cols = len(data[0])
    points = {}
    for y in range(rows):
        for x in range(cols):
            c = data[y][x]
            if c != "#":
                points[(x, y)] = "."
    start = (1, 0)
    neighbors = defaultdict(dict)
    q = [start]
    seen = set()
    while len(q) > 0:
        origin = q.pop(0)
        seen.add(origin)
        n = get_neighbors(origin[0], origin[1], points)
        for neighbor in n:
            next_intersection, distance = get_next_intersection(origin, neighbor, points)
            neighbors[origin][next_intersection] = distance
            if next_intersection not in seen:
                q.append(next_intersection)

    q = [(0, 1, 0, set())]
    target = (cols - 2, rows - 1)
    best = {(1, 0): 0}
    while len(q) > 0:
        d, x, y, seen = heapq.heappop(q)
        if len(q) % 100 == 0:
            print(len(q), d)
        p_neighbors = [(n, distance) for n, distance in neighbors[(x, y)].items() if (n[0], n[1]) not in seen and path_to_end_exists((n[0], n[1]), target, neighbors, seen)]
        for (nx, ny), distance in p_neighbors:
            heapq.heappush(q, (d + distance, nx, ny, seen.union([(x, y)])))
            best[(nx, ny)] = d + distance
    ans = best[target]
    print(ans)


task1()
task2()
