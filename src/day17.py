from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 17

def get_neighbors(x, y, x_max, y_max, direction):
    neighbors = {}
    if 0 <= x - 1 and direction[0] != "right":
        neighbors["left"] = (x - 1, y)
    if x + 1 <= x_max and direction[0] != "left":
        neighbors["right"] = (x + 1, y)
    if 0 <= y - 1 and direction[0] != "down":
        neighbors["up"] = (x, y - 1)
    if y + 1 <= y_max and direction[0] != "up":
        neighbors["down"] = (x, y + 1)
    if direction[1] == 3 and direction[0] in neighbors:
        del neighbors[direction[0]]
    return neighbors

def heuristic(x, y, goal, cost):
    d = abs(goal[0] - x) + abs(goal[1] - y)
    return d + cost

def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    costs = {}
    rows = len(data)
    cols = len(data[0])
    for y in range(rows):
        for x in range(cols):
            costs[(x, y)] = int(data[y][x])
    positions = {(0, 0, ("right", 0), 0)} # x, y, direction, squares traveled in direction, cost
    best_seen = {}
    best = sum(v for k, v in costs.items() if k[1] == 0 or k[0] == cols - 1) * 2
    goal = (cols - 1, rows - 1)
    while len(positions) > 0:
        new_positions = set()
        for x, y, direction, cost in positions:
            neighbors = get_neighbors(x, y, cols - 1, rows - 1, direction)
            for n_direction, neighbor in sorted(neighbors.items(), key=lambda x: (x[1][0], x[1][1])):
                n_cost = cost + costs[(neighbor[0], neighbor[1])]
                h = heuristic(x, y, goal, n_cost)
                if direction[0] == n_direction:
                    n_direction = (n_direction, direction[1] + 1)
                else:
                    n_direction = (n_direction, 1)
                k = (neighbor[0], neighbor[1], n_direction)
                if (k not in best_seen or best_seen[k] > n_cost) and h <= best:
                    new_positions.add((*k, n_cost))
                    best_seen[k] = n_cost
                    if neighbor == goal:
                        best = n_cost
        print(len(positions))
    goal_costs = { v for k, v in best_seen.items() if k[0] == goal[0] and k[1] == goal[1] }
    ans = min(goal_costs)
    print(ans)


def get_neighbors2(x, y, x_max, y_max, direction):
    neighbors = {}
    def distance_needed(direction, current_direction):
        if direction == current_direction[0]:
            return max(1, 4 - current_direction[1])
        return 4
    if 0 <= x - distance_needed("left", direction) and direction[0] != "right":
        neighbors["left"] = (x - 1, y)
    if x + distance_needed("right", direction) <= x_max and direction[0] != "left":
        neighbors["right"] = (x + 1, y)
    if 0 <= y - distance_needed("up", direction) and direction[0] != "down":
        neighbors["up"] = (x, y - 1)
    if y + distance_needed("down", direction) <= y_max and direction[0] != "up":
        neighbors["down"] = (x, y + 1)
    if direction[1] == 10 and direction[0] in neighbors:
        del neighbors[direction[0]]
    if direction[1] < 4:
        neighbors = {k: v for k, v in neighbors.items() if k == direction[0]}
    return neighbors

def task2():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    costs = {}
    rows = len(data)
    cols = len(data[0])
    for y in range(rows):
        for x in range(cols):
            costs[(x, y)] = int(data[y][x])
    q = [(0, 0, ("right", 0), 0), (0, 0, ("down", 0), 0)] # x, y, direction, squares traveled in direction, cost
    best_seen = {}
    best = sum(v for k, v in costs.items() if k[1] == 0 or k[0] == cols - 1) * 10
    goal = (cols - 1, rows - 1)
    while len(q) > 0:
        x, y, direction, cost = q.pop()
        neighbors = get_neighbors2(x, y, cols - 1, rows - 1, direction)
        for n_direction, neighbor in neighbors.items():
            n_cost = cost + costs[(neighbor[0], neighbor[1])]
            h = heuristic(x, y, goal, n_cost)
            if direction[0] == n_direction:
                n_direction = (n_direction, direction[1] + 1)
            else:
                n_direction = (n_direction, 1)
            k = (neighbor[0], neighbor[1], n_direction)
            if (k not in best_seen or best_seen[k] > n_cost) and h <= best:
                best_seen[k] = n_cost
                q.append((*k, n_cost))
                if neighbor == goal:
                    best = n_cost
        print(len(q))
    goal_costs = { v for k, v in best_seen.items() if k[0] == goal[0] and k[1] == goal[1] }
    ans = min(goal_costs)
    print(ans)


task1()
# task2()
