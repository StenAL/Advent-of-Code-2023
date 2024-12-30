from util import *
from collections import *
import copy
from functools import reduce
from math import prod
from itertools import combinations

day = 24


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    stones = []
    for line in data:
        position, velocity = line.split(" @ ")
        positions = [int(e) for e in position.split(", ")]
        velocities = [int(e) for e in velocity.split(", ")]
        stones.append((positions, velocities))

    min_coord = 200000000000000
    max_coord = 400000000000000
    zone_intersections = 0
    for s1 in stones:
        x1, y1, z1 = s1[0]
        v1_x, v1_y, v1_z = s1[1]
        for s2 in stones:
            x2, y2, z2 = s2[0]
            v2_x, v2_y, v2_z = s2[1]
            if s1 == s2:
                continue
            # need to find t such that
            # x satisfies x1 + v1_x * t1 and x2 + v2_x * t2
            # x1 + v1_x * t1 == x2 + v2_x * t2 ==> t1 * v1_x == x2 + v2_x * t2 - x1 ==> t1 == (x2 + v2_x * t2 - x1) / v1_x
            # y1 + v1_y * t1 == y2 + v2_y * t2 ==> .................................... t1 == (y2 + v2_y * t2 - y1) / v1_y
            # v1_y * (x2 + v2_x * t2 - x1) == v1_x * (y2 + v2_y * t2 - y1)
            # v1_y * x2 + v2_x * t2 * v1_y - x1 * v1_y == v1_x * y2 + v2_y * t2 * v1_x - y1 * v1_x
            # v2_x * t2 * v1_y - v2_y * t2 * v1_x == v1_x * y2 - y1 * v1_x - v1_y * x2 + x1 * v1_y
            # t2 (v2_x * v1_y - v2_y * v1_x) == ...
            # t2 == (v1_x * y2 - y1 * v1_x - v1_y * x2 + x1 * v1_y) / (v2_x * v1_y - v2_y * v1_x)
            if v2_x * v1_y - v2_y * v1_x == 0:  # parallel
                continue
            t2 = (v1_x * y2 - y1 * v1_x - v1_y * x2 + x1 * v1_y) / (
                v2_x * v1_y - v2_y * v1_x
            )
            t1 = (x2 + v2_x * t2 - x1) / v1_x
            if t2 < 0 or t1 < 0:
                continue
            x = x2 + v2_x * t2
            y = y2 + v2_y * t2
            if min_coord <= x <= max_coord and min_coord <= y <= max_coord:
                zone_intersections += 1
    ans = zone_intersections // 2
    print(ans)


def get_intersection_point(s1, s2):
    x1, y1, z1 = s1[0]
    v1_x, v1_y, v1_z = s1[1]
    x2, y2, z2 = s2[0]
    v2_x, v2_y, v2_z = s2[1]
    # need to find x, y such that
    # x satisfies x1 + v1_x * t1 and x2 + v2_x * t2
    # x1 + v1_x * t1 == x2 + v2_x * t2 ==> t1 * v1_x == x2 + v2_x * t2 - x1 ==> t1 == (x2 + v2_x * t2 - x1) / v1_x
    # y1 + v1_y * t1 == y2 + v2_y * t2 ==> .................................... t1 == (y2 + v2_y * t2 - y1) / v1_y
    # v1_y * (x2 + v2_x * t2 - x1) == v1_x * (y2 + v2_y * t2 - y1)
    # v1_y * x2 + v2_x * t2 * v1_y - x1 * v1_y == v1_x * y2 + v2_y * t2 * v1_x - y1 * v1_x
    # v2_x * t2 * v1_y - v2_y * t2 * v1_x == v1_x * y2 - y1 * v1_x - v1_y * x2 + x1 * v1_y
    # t2 (v2_x * v1_y - v2_y * v1_x) == ...
    # t2 == (v1_x * y2 - y1 * v1_x - v1_y * x2 + x1 * v1_y) / (v2_x * v1_y - v2_y * v1_x)
    if v2_x * v1_y - v2_y * v1_x == 0:  # parallel, all points itersect
        return None
    t2 = (v1_x * y2 - y1 * v1_x - v1_y * x2 + x1 * v1_y) / (v2_x * v1_y - v2_y * v1_x)
    x = x2 + v2_x * t2
    y = y2 + v2_y * t2
    return x, y


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    hailstones = []
    for line in data:
        position, velocity = line.split(" @ ")
        positions = [int(e) for e in position.split(", ")]
        velocities = [int(e) for e in velocity.split(", ")]
        hailstones.append((positions, velocities))

    stone = None
    v1 = 0
    while stone is None:
        # print(v1)
        for v2 in range(v1 + 1):
            velocities = {
                (v1, v2),
                (v1, -v2),
                (-v1, v2),
                (-v1, -v2),
                (v2, v1),
                (v2, -v1),
                (-v2, v1),
                (-v2, -v1),
            }
            for vx, vy in velocities:
                adjusted_hailstones = []
                for hailstone in hailstones:
                    x1, y1, z1 = hailstone[0]
                    v1_x, v1_y, v1_z = hailstone[1]
                    v1_x = v1_x - vx
                    v1_y = v1_y - vy
                    adjusted_hailstones.append(((x1, y1, z1), (v1_x, v1_y, v1_z)))
                intersection_points = set()
                for pair in combinations(adjusted_hailstones, 2):
                    p = get_intersection_point(pair[0], pair[1])
                    if p is None:
                        continue
                    intersection_points.add(p)
                    if len(intersection_points) > 1:
                        break
                if len(intersection_points) == 1:
                    origin = next(iter(intersection_points)) + (-1,)
                    stone = (origin, (vx, vy, -1))
        v1 += 1

    x, y, _ = stone[0]
    vx, vy, _ = stone[1]

    vz = 0
    z = -1
    while z == -1:
        adjusted_hailstones = []
        for hailstone in hailstones:
            x1, y1, z1 = hailstone[0]
            v1_x, v1_y, v1_z = hailstone[1]
            v1_x = v1_x - vx
            v1_y = v1_y - vy
            v1_z = v1_z - vz
            adjusted_hailstones.append(((x1, z1, z1), (v1_x, v1_z, v1_z)))
        intersection_points = set()
        for pair in combinations(adjusted_hailstones, 2):
            p = get_intersection_point(pair[0], pair[1])
            if p is None:
                continue
            intersection_points.add(p)
            if len(intersection_points) > 1:
                break
        if len(intersection_points) == 1:
            _, z = next(iter(intersection_points))
        vz += 1
    origin = (x, y, z)
    ans = int(sum(origin))
    print(ans)


task1()
task2()
