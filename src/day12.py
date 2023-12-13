from util import *
from collections import *
import copy
from functools import reduce
from math import prod
import re

day = 12


def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    ans = 0
    for line in data:
        springs, sequences = line.split()
        sequences = [int(n) for n in sequences.split(",")]
        candidates = { springs }
        for i in range(len(springs)):
            c = springs[i]
            if c == "?":
                new_candidates = set()
                for candidate in candidates:
                    new_candidates.add(candidate[:i] + "." + candidate[i + 1:])
                    new_candidates.add(candidate[:i] + "#" + candidate[i + 1:])
                candidates = new_candidates
        for candidate in candidates:
            sequence = []
            sequential = 0
            for c in candidate:
                if c == "#":
                    sequential += 1
                else:
                    if sequential != 0:
                        sequence.append(sequential)
                    sequential = 0
            if sequential != 0:
                sequence.append(sequential)
            if sequence == sequences:
                ans += 1
    print(ans)

def get_possible_groups(springs, memo, sequence):
    #print(f"called with {springs}")
    if springs in memo:
        return memo[springs]
    if len(springs) == 1:
        if springs == "#":
            return {((1,), "#"): 1}
        elif springs == ".":
            return {((), "."): 1}
        else:
            return {((), "."): 1, ((1,), "#"): 1}
    new_groups = {}
    if springs.endswith("."):
        groups = get_possible_groups(springs[:-1], memo, sequence)
        for k, v in groups.items():
            if (k[0], ".") in new_groups:
                new_groups[(k[0], ".")] += v
            else: 
                new_groups[(k[0], ".")] = v
    elif springs.endswith("#"):
        groups = get_possible_groups(springs[:-1], memo, sequence)
        for k, v in groups.items():
            if k[1] == "#":
                new_key = ((*k[0][:-1], k[0][-1] + 1), "#")
                new_groups[new_key] = v
            else:
                new_key = (k[0] + (1,), "#")
                new_groups[new_key] = v
    else:
        new_groups = get_possible_groups(springs[:-1] + "#", memo, sequence).copy()
        g2 = get_possible_groups(springs[:-1] + ".", memo, sequence)
        for k,v in g2.items():
            if k in new_groups:
                print("aaa")
                new_groups[k] += v
            else:
                new_groups[k] = v
    new_groups = {k:v for k,v in new_groups.items() if len(k[0]) <= len(sequence) and sequence[:max(len(k[0]) - 1, 0)] == k[0][:-1]}
    memo[springs] = new_groups
    return new_groups


def task2():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    ans = 0
    scale = 5
    for line in data:
        springs, groups = line.split()
        springs = "?".join([springs] * scale)
        springs = re.sub("\\.+", ".", springs)
        memo = defaultdict(lambda: defaultdict(int))
        groups = tuple([int(n) for n in groups.split(",")] * scale)
        possible_groups = get_possible_groups(springs, memo, groups)

        matches = possible_groups.get((groups, "#"), 0) + possible_groups.get((groups, "."), 0)
        ans += matches
    print(ans)

task1()
task2()
