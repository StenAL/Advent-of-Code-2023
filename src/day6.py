from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 6


def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    times = [int(i) for i in data[0].split(":")[1].split()]
    distances = [int(i) for i in data[1].split(":")[1].split()]
    wins = []
    for race in range(len(times)):
        time = times[race]
        winning_strategies = 0
        for speed in range(time + 1):
            time_traveled = time - speed
            distance = speed * time_traveled
            if distance > distances[race]:
                winning_strategies += 1
        wins.append(winning_strategies)
    ans = prod(wins)
    print(ans)


def task2():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    time = int("".join(i for i in data[0].split(":")[1].split()))
    distance = int("".join(i for i in data[1].split(":")[1].split()))
    wins = 0
    for speed in range(time + 1):
        time_traveled = time - speed
        traveled_distance = speed * time_traveled
        if traveled_distance > distance:
            wins += 1
    print(wins)


task1()
task2()

