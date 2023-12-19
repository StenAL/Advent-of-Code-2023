from util import *
from collections import *
import copy
from functools import reduce
from math import prod
import re

day = 19


def task1():
    data = get_input_for_day(day, "\n\n")
    #data = get_input_for_file("test", "\n\n")
    rules_data, parts_data = data

    rules = defaultdict(list)
    for rule in rules_data.split():
        name, content = rule.split("{")
        content = content.strip("}").split(",")
        for test in content:
            if ":" in test:
                condition, dst = test.split(":")
                m = re.match("(.*)(<|>)(.*)", condition)
                category, operator, v = m.group(1), m.group(2), m.group(3)
                rules[name].append((category, operator, int(v), dst))
            else:
                dst = test
                rules[name].append((dst))
    parts = []
    for part_data in parts_data.split():
        part = {}
        part_data = part_data.strip("{").strip("}").split(",")
        for c in part_data:
            category, v = c.split("=")
            v = int(v)
            part[category] = v
        parts.append(part)
    accepted = []
    for part in parts:
        rule_key = "in"
        while rule_key not in ["R", "A"]:
            rule = rules[rule_key]
            for test in rule:
                if len(test) == 4:
                    category, operator, v, dst = test
                    if (operator == ">" and part[category] > v) or (operator == "<" and part[category] < v):
                        rule_key = dst
                        break
                else:
                    rule_key = test
        if rule_key == "A":
            accepted.append(part)
    ans = sum(sum(p.values()) for p in accepted)
    print(ans)


def task2():
    data = get_input_for_day(day, "\n\n")
    #data = get_input_for_file("test", "\n\n")
    rules_data, parts_data = data

    rules = defaultdict(list)
    for rule in rules_data.split():
        name, content = rule.split("{")
        content = content.strip("}").split(",")
        for test in content:
            if ":" in test:
                condition, dst = test.split(":")
                m = re.match("(.*)(<|>)(.*)", condition)
                category, operator, v = m.group(1), m.group(2), m.group(3)
                rules[name].append((category, operator, v, dst))
            else:
                dst = test
                rules[name].append((dst))

    parts = []
    for part_data in parts_data.split():
        part = {}
        part_data = part_data.strip("{").strip("}").split(",")
        for c in part_data:
            category, v = c.split("=")
            v = int(v)
            part[category] = v
        parts.append(part)

    q = [([], "A")] # conditions, target
    valid_parts = []
    while len(q) > 0:
        conditions, target = q.pop()
        if target == "in":
            valid_parts.append(conditions)
            continue
        for name, rule in rules.items():
            for i in range(len(rule)):
                test = rule[i]
                if len(test) == 4:
                    category, operator, v, dst = test
                    if dst == target:
                        false_conditions = ["!" + "".join(e[:3]) for e in rule[:i]]
                        true_condition = category + operator + v
                        new_conditions = [*conditions, *false_conditions, true_condition]
                        q.append((new_conditions, name))
                else:
                    if test == target:
                        false_conditions = ["!" + "".join(e[:3]) for e in rule[:i]]
                        new_conditions = [*conditions, *false_conditions]
                        q.append((new_conditions, name))
    ans = 0
    for conditions in valid_parts:
        valid_ranges = { "x": [1, 4001], "m": [1, 4001], "a": [1, 4001], "s": [1, 4001] }
        for test in conditions:
            negated = test.startswith("!")
            test = test.strip("!")
            m = re.match("(.*)(<|>)(.*)", test)
            category, operator, v = m.group(1), m.group(2), m.group(3)
            if not negated and operator == ">":
                valid_ranges[category][0] = max(valid_ranges[category][0], int(v) + 1)
            if negated and operator == "<":
                valid_ranges[category][0] = max(valid_ranges[category][0], int(v))
            if not negated and operator == "<":
                valid_ranges[category][1] = min(valid_ranges[category][1], int(v))
            if negated and operator == ">":
                valid_ranges[category][1] = min(valid_ranges[category][1], int(v) + 1)
        ans += prod(r[1] - r[0] for r in valid_ranges.values())
    print(ans)

task1()
task2()
