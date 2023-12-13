from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 13


def task1():
    f = open("input/day" + str(day) + ".txt")
    #f = open("input/test.txt")
    patterns = [p.split() for p in f.read().split("\n\n")]
    ans = 0
    for pattern in patterns:
        l = len(pattern)
        for i in range(l):
            maybe_sym = pattern[i:]
            if len(maybe_sym) > 1 and len(maybe_sym) % 2 == 0 and all(maybe_sym[j] == maybe_sym[len(maybe_sym) - 1 - j] for j in range(len(maybe_sym))):
                midway = len(maybe_sym) // 2 + i
                #print(f"{patterns.index(pattern)}: (cut top), {midway} {pattern[midway]} {pattern[midway - 1]}")
                ans += midway * 100
        for i in range(l):
            maybe_sym = pattern[:len(pattern) - i]
            if len(maybe_sym) > 1 and len(maybe_sym) % 2 == 0 and all(maybe_sym[j] == maybe_sym[len(maybe_sym) - 1 - j] for j in range(len(maybe_sym))):
                midway = len(maybe_sym) // 2
                #print(f"{patterns.index(pattern)}: (cut bottom), {midway} {pattern[midway]} {pattern[midway - 1]}")
                ans += midway * 100
        transposed = list(zip(*pattern))
        l = len(transposed)
        for i in range(l):
            maybe_sym = transposed[i:]
            if len(maybe_sym) > 1 and len(maybe_sym) % 2 == 0 and all(maybe_sym[j] == maybe_sym[len(maybe_sym) - 1 - j] for j in range(len(maybe_sym))):
                midway = len(maybe_sym) // 2 + i
                #print(f"{patterns.index(pattern)}: (cut left), {midway} {"".join(transposed[midway])}")
                ans += midway
        for i in range(l):
            maybe_sym = transposed[:len(transposed) - i]
            if len(maybe_sym) > 1 and len(maybe_sym) % 2 == 0 and all(maybe_sym[j] == maybe_sym[len(maybe_sym) - 1 - j] for j in range(len(maybe_sym))):
                midway = len(maybe_sym) // 2
                #print(f"{patterns.index(pattern)}: (cut right), {midway} {"".join(transposed[midway])}")
                ans += midway
    print(ans)


def get_diffs(maybe_sym):
    diffs = []
    for e1, e2 in zip(maybe_sym, maybe_sym[::-1]):
        diff_count = 0
        for c1, c2 in zip(e1, e2):
            if c1 != c2:
                diff_count += 1
        diffs.append(diff_count)
    return diffs

def task2():
    f = open("input/day" + str(day) + ".txt")
    #f = open("input/test.txt")
    patterns = [p.split() for p in f.read().split("\n\n")]
    ans = 0
    for pattern in patterns:
        l = len(pattern)
        for i in range(l):
            maybe_sym = pattern[i:]
            diffs = get_diffs(maybe_sym)
            one_count = diffs.count(1)
            if len(maybe_sym) > 1 and len(maybe_sym) % 2 == 0 and one_count == 2 and diffs.count(0) == len(maybe_sym) - 2:
                midway = len(maybe_sym) // 2 + i
                # print(f"{patterns.index(pattern)}: (cut top), {midway} {pattern[midway]} {pattern[midway - 1]}")
                ans += midway * 100
        for i in range(l):
            maybe_sym = pattern[:len(pattern) - i]
            diffs = get_diffs(maybe_sym)
            one_count = diffs.count(1)
            if len(maybe_sym) > 1 and len(maybe_sym) % 2 == 0 and one_count == 2 and diffs.count(0) == len(maybe_sym) - 2:
                midway = len(maybe_sym) // 2
                # print(f"{patterns.index(pattern)}: (cut bottom), {midway} {pattern[midway]} {pattern[midway - 1]}")
                ans += midway * 100
        transposed = list(zip(*pattern))
        l = len(transposed)
        for i in range(l):
            maybe_sym = transposed[i:]
            diffs = get_diffs(maybe_sym)
            one_count = diffs.count(1)
            if len(maybe_sym) > 1 and len(maybe_sym) % 2 == 0 and one_count == 2 and diffs.count(0) == len(maybe_sym) - 2:
                midway = len(maybe_sym) // 2 + i
                #print(f"{patterns.index(pattern)}: (cut left), {midway} {"".join(transposed[midway])}")
                ans += midway
        for i in range(l):
            maybe_sym = transposed[:len(transposed) - i]
            diffs = get_diffs(maybe_sym)
            one_count = diffs.count(1)
            if len(maybe_sym) > 1 and len(maybe_sym) % 2 == 0 and one_count == 2 and diffs.count(0) == len(maybe_sym) - 2:
                midway = len(maybe_sym) // 2
                #print(f"{patterns.index(pattern)}: (cut right), {midway} {"".join(transposed[midway])}")
                ans += midway
    print(ans)


task1() 
task2()
