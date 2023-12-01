from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 1


def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    data = ["".join(c for c in s if c.isnumeric()) for s in data]
    ans = sum([int(e[0] + e[-1]) for e in data])
    print(ans)


def task2():
    data = get_input_for_day(day)
    #data = get_input_for_file("test2")
    replacements = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                    "six": "6", "seven": "7", "eight": "8", "nine": "9" }
    new_data = []
    for s in data:
        new_s = ""
        for i in range(len(s)):
            new_s += s[i]
            for k,v in replacements.items():
                new_s = new_s.replace(k, v + k)
        new_data.append(new_s)
    data = new_data
    data = ["".join(c for c in s if c.isnumeric()) for s in data]
    ans = sum([int(e[0] + e[-1]) for e in data])
    print(ans)


task1()
task2()
