from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 4


def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    ans = 0
    for line in data:
        winners, actual = line.split(" | ")
        winners = set(int(n) for n in winners.split(": ")[1].split(" ") if n != "")
        actual = set(int(n) for n in actual.split(" ") if n != "")
        overlap = len(winners.intersection(actual))
        if overlap > 0:
            points = 2 ** (overlap - 1)
            ans += points
    print(ans)
        


def task2():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    ans = 0
    counts = [1] * len(data)
    for i in range(len(data)):
        line = data[i]
        winners, actual = line.split(" | ")
        winners = set(int(n) for n in winners.split(": ")[1].split(" ") if n != "")
        actual = set(int(n) for n in actual.split(" ") if n != "")
        overlap = len(winners.intersection(actual))
        for j in range(overlap):
            counts[i + j + 1] += counts[i]
    ans = sum(counts)
    print(ans)



task1()
task2()
