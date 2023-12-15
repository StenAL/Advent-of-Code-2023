from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 15


def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    ans = 0
    for line in data:
        entries = line.split(",")
        for entry in entries:
            ascii_order = [ord(c) for c in entry]
            val = 0
            for e in ascii_order:
                val += e
                val *= 17
            val = val % 256
            ans += val
    print(ans)

def hash_algorithm(s):
    ascii_order = [ord(c) for c in s]
    val = 0
    for e in ascii_order:
        val += e
        val *= 17
    val = val % 256
    return val
    

def task2():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    entries = data[0].split(",")
    boxes = defaultdict(list)
    lengths = {}
    for entry in entries:
        if "=" in entry:
            label, focus_length = entry.split("=")
            hash_value = hash_algorithm(label)
            box = boxes[hash_value]
            focus_length = int(focus_length)
            lengths[label] = focus_length
            if label in box:
                continue
            else:
                box.append(label)
        if "-" in entry:
            label = entry.strip("-")
            hash_value = hash_algorithm(label)
            box = boxes[hash_value]
            if label in box:
                box.remove(label)

    ans = 0
    for box_number, lenses in boxes.items():
        for i, lens in enumerate(lenses):
            power = (box_number + 1) * (i + 1) * lengths[lens]
            ans += power
    print(ans)


task1()
task2()
