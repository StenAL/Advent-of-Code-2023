from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 2


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    max_red = 12
    max_green = 13
    max_blue = 14
    ans = 0
    for line in data:
        impossible = False
        game_id, cubes = line.split(": ")
        game_id = int(game_id.split(" ")[1])
        for turn in cubes.split("; "):
            for color in turn.split(", "):
                amount, color = color.split(" ")
                if color == "red" and int(amount) > max_red:
                    impossible = True
                if color == "green" and int(amount) > max_green:
                    impossible = True
                if color == "blue" and int(amount) > max_blue:
                    impossible = True
        if not impossible:
            ans += game_id
    print(ans)
def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    ans = 0
    for line in data:
        max_red = 1
        max_green = 1
        max_blue = 1
        game_id, cubes = line.split(": ")
        for turn in cubes.split("; "):
            for color in turn.split(", "):
                amount, color = color.split(" ")
                if color == "red":
                    max_red = max(max_red, int(amount))
                if color == "green":
                    max_green = max(max_green, int(amount))
                if color == "blue":
                    max_blue = max(max_blue, int(amount))
        ans += max_red * max_blue * max_green
    print(ans)


task1()
task2()
