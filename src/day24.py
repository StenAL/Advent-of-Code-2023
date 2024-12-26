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
                # print(s1, s2, "cross at", x, y)
    ans = zone_intersections // 2
    print(ans)


def get_intersection_point(s1, s2):
    x1, y1, z1 = s1[0]
    v1_x, v1_y, v1_z = s1[1]
    x2, y2, z2 = s2[0]
    v2_x, v2_y, v2_z = s2[1]
    if s1 == s2:
        return
    # need to find x, y such that
    # x satisfies x1 + v1_x * t1 and x2 + v2_x * t2
    # x1 + v1_x * t1 == x2 + v2_x * t2 ==> t1 * v1_x == x2 + v2_x * t2 - x1 ==> t1 == (x2 + v2_x * t2 - x1) / v1_x
    # y1 + v1_y * t1 == y2 + v2_y * t2 ==> .................................... t1 == (y2 + v2_y * t2 - y1) / v1_y
    # v1_y * (x2 + v2_x * t2 - x1) == v1_x * (y2 + v2_y * t2 - y1)
    # v1_y * x2 + v2_x * t2 * v1_y - x1 * v1_y == v1_x * y2 + v2_y * t2 * v1_x - y1 * v1_x
    # v2_x * t2 * v1_y - v2_y * t2 * v1_x == v1_x * y2 - y1 * v1_x - v1_y * x2 + x1 * v1_y
    # t2 (v2_x * v1_y - v2_y * v1_x) == ...
    # t2 == (v1_x * y2 - y1 * v1_x - v1_y * x2 + x1 * v1_y) / (v2_x * v1_y - v2_y * v1_x)
    if v2_x * v1_y - v2_y * v1_x == 0:  # parallel
        return None
    t2 = (v1_x * y2 - y1 * v1_x - v1_y * x2 + x1 * v1_y) / (v2_x * v1_y - v2_y * v1_x)
    # t1 = (x2 + v2_x * t2 - x1) / v1_x
    # if t2 < 0 or t1 < 0:
    # return 2,2
    x = x2 + v2_x * t2
    y = y2 + v2_y * t2
    # print(s1, s2, "cross at", x, y)
    return x, y


def get_intersection_point2(s1, s2):
    x1, y1, z1 = s1[0]
    v1_x, v1_y, v1_z = s1[1]
    x2, y2, z2 = s2[0]
    v2_x, v2_y, v2_z = s2[1]
    if s1 == s2:
        return
    if v2_x * v1_z - v2_z * v1_x == 0:  # parallel
        return None
    t2 = (v1_x * z2 - z1 * v1_x - v1_z * x2 + x1 * v1_z) / (v2_x * v1_z - v2_z * v1_x)
    # t1 = (x2 + v2_x * t2 - x1) / v1_x
    x = x2 + v2_x * t2
    z = z2 + v2_z * t2
    # print(s1, s2, "cross at", x, y)
    return x, z


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    stones = []
    for line in data:
        position, velocity = line.split(" @ ")
        positions = [int(e) for e in position.split(", ")]
        velocities = [int(e) for e in velocity.split(", ")]
        stones.append((positions, velocities))

    # either vx < 0 in which case x > max(x for x in formula where vx > 0)
    highest_positive_vx = max([s[0][0] for s in stones if s[1][0] > 0])
    # or vx > 0 in which case x < min(x for x in formula where vx < 0)
    lowest_negative_vx = min([s[0][0] for s in stones if s[1][0] < 0])
    # vy_pos = (max([s[0][1] for s in stones if s[1][1] > 0]))
    # vy_neg = (min([s[0][1] for s in stones if s[1][1] < 0]))
    # vz_pos = (max([s[0][2] for s in stones if s[1][2] > 0]))
    # vz_neg = (min([s[0][2] for s in stones if s[1][2] < 0]))
    fastest_positive_above_lowest_negative = max(
        [s[1][0] for s in stones if s[1][0] > 0 and s[0][0] > lowest_negative_vx]
    )
    fastest_negative_below_highest_positive = min(
        [s[1][0] for s in stones if s[1][0] < 0 and s[0][0] < highest_positive_vx]
    )
    # print(f"if vx < 0: minimum start={highest_positive_vx}, vx < {fastest_negative_below_highest_positive}")
    # print(f"if vx > 0: maximum start={lowest_negative_vx}, vx > {fastest_positive_above_lowest_negative}")
    # at t1, (x + t1 * vx, y + t1 * vy, z + t1 * vz) == (x1 + t1*v1x,y1 +t1*v1y,z1+t1*v1z)
    search_range = 250
    result = None
    vx = -1
    vy = -1
    for vx in range(-search_range, search_range):
        if result is not None:
            break
        # if vx % 10 == 0:
        # print(vx)
        for vy in range(-search_range, search_range):
            adjusted_stones = []
            for stone in stones:
                x1, y1, z1 = stone[0]
                v1_x, v1_y, v1_z = stone[1]
                v1_x = v1_x - vx
                v1_y = v1_y - vy
                adjusted_stones.append(((x1, y1, z1), (v1_x, v1_y, v1_z)))
            intersects = set()
            for pair in combinations(adjusted_stones, 2):
                p = get_intersection_point(pair[0], pair[1])
                # print(pair, p)
                intersects.add(p)
                if len(intersects) > 2:
                    break
            # if vx == -3 and vy == 1:
            if len(intersects) <= 2:
                # print(intersects, vx, vy)
                result = [e for e in intersects if e is not None][0]
                result = (result, (vx, vy))

    origin = result[0]
    vx, vy = result[1]
    for vz in range(-search_range, search_range):
        adjusted_stones = []
        for stone in stones:
            x1, y1, z1 = stone[0]
            v1_x, v1_y, v1_z = stone[1]
            v1_x = v1_x - vx
            v1_y = v1_y - vy
            v1_z = v1_z - vz
            adjusted_stones.append(((x1, y1, z1), (v1_x, v1_y, v1_z)))
        intersects = set()
        for pair in combinations(adjusted_stones, 2):
            p = get_intersection_point2(pair[0], pair[1])
            # print(pair, p)
            intersects.add(p)
            if len(intersects) > 2:
                break
        # print(vz, intersects)
        if len(intersects) <= 2:
            # print(intersects, vx, vy, vz)
            result = [e for e in intersects if e is not None][0]
            break
    origin = origin + (result[1],)
    # print(origin)
    ans = int(sum(origin))
    print(ans)


task1()
task2()
