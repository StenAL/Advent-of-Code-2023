from util import *
from collections import *
import copy
from functools import reduce
from math import prod, lcm

day = 8


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    parse_mode = "directions"
    neighbors = {}
    directions = []
    for line in data:
        if line == "":
            parse_mode = "neighbors"
            continue
        if parse_mode == "directions":
            directions = list(line)
        elif parse_mode == "neighbors":
            node, lr = line.split(" = ")
            l, r = lr.strip("(").strip(")").split(", ")
            neighbors[node] = (l, r)
    current_node = "AAA"
    steps = 0
    while current_node != "ZZZ":
        move = directions[(steps % len(directions))]
        l, r = neighbors[current_node]
        current_node = l if move == "L" else r
        steps += 1
    ans = steps
    print(ans)




def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    parse_mode = "directions"
    neighbors = {}
    directions = []
    for line in data:
        if line == "":
            parse_mode = "neighbors"
            continue
        if parse_mode == "directions":
            directions = list(line)
        elif parse_mode == "neighbors":
            node, lr = line.split(" = ")
            l, r = lr.strip("(").strip(")").split(", ")
            neighbors[node] = (l, r)
    current_nodes = { n for n in neighbors if n.endswith("A") }
    steps_to_reach_end = set()
    steps = 0
    while len(current_nodes) > 0:
        new_nodes = set()
        move = directions[(steps % len(directions))]
        steps += 1
        for current_node in current_nodes:
            l, r = neighbors[current_node]
            current_node = l if move == "L" else r
            if current_node.endswith("Z"):
                steps_to_reach_end.add(steps)
            else:
                new_nodes.add(current_node)
        current_nodes = new_nodes
    ans = lcm(*steps_to_reach_end)
    print(ans)


task1()
task2()
