from util import *
from collections import *
import copy
from functools import reduce
from math import prod, lcm

day = 20


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test2")
    modules = {} # name -> type, destinations
    flipflop_states = {}
    conjunction_states = {}
    reverse_destinations = defaultdict(list)
    for line in data:
        module, destinations = line.split(" -> ")
        destinations = destinations.split(", ")
        module_type = module[0] if module[0] in "%&" else "broadcaster"
        module = module[1:] if module[0] in "%&" else "broadcaster"
        modules[module] = (module_type, destinations)
        if module_type == "%":
            flipflop_states[module] = "off"
        elif module_type == "&":
            conjunction_states[module] = {}
        for d in destinations:
            reverse_destinations[d].append(module) 
    
    for conjunction_module in conjunction_states:
        for d in reverse_destinations[conjunction_module]:
            conjunction_states[conjunction_module][d] = "l"
    low_pulses = 0
    high_pulses = 0
    cycles = 1000
    for _ in range(cycles):
        q = [("button", "broadcaster", "l")]
        while len(q) > 0:
            source, module, signal = q.pop()
            if signal == "l":
                low_pulses += 1
            else:
                high_pulses += 1
            if module not in modules:
                continue
            module_type, destinations = modules[module]
            if module_type == "broadcaster":
                q += [(module, d, signal) for d in destinations]
            elif module_type == "%":
                if signal == "h":
                    continue
                module_state = flipflop_states[module]
                q += [(module, d, "h" if module_state == "off" else "l") for d in destinations]
                flipflop_states[module] = "off" if module_state == "on" else "on"
            elif module_type == "&":
                conjunction_states[module][source] = signal
                pulse = "l" if set(conjunction_states[module].values()) == { "h" } else "h"
                q += [(module, d, pulse) for d in destinations]
            
    ans = low_pulses * high_pulses
    print(ans)

def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test2")
    modules = {} # name -> type, destinations
    flipflop_states = {}
    conjunction_states = {}
    reverse_destinations = defaultdict(list)
    for line in data:
        module, destinations = line.split(" -> ")
        destinations = destinations.split(", ")
        module_type = module[0] if module[0] in "%&" else "broadcaster"
        module = module[1:] if module[0] in "%&" else "broadcaster"
        modules[module] = (module_type, destinations)
        if module_type == "%":
            flipflop_states[module] = "off"
        elif module_type == "&":
            conjunction_states[module] = {}
        for d in destinations:
            reverse_destinations[d].append(module) 
    
    for conjunction_module in conjunction_states:
        for d in reverse_destinations[conjunction_module]:
            conjunction_states[conjunction_module][d] = "l"
    cycles = 50000
    prereq_seen = defaultdict(list)
    for i in range(cycles):
        q = [("button", "broadcaster", "l")]
        while len(q) > 0:
            source, module, signal = q.pop(0)
            if module not in modules:
                continue
            module_type, destinations = modules[module]
            if module_type == "broadcaster":
                q += [(module, d, signal) for d in destinations]
            elif module_type == "%":
                if signal == "h":
                    continue
                module_state = flipflop_states[module]
                q += [(module, d, "h" if module_state == "off" else "l") for d in destinations]
                flipflop_states[module] = "off" if module_state == "on" else "on"
            elif module_type == "&":
                conjunction_states[module][source] = signal
                pulse = "l" if set(conjunction_states[module].values()) == { "h" } else "h"
                q += [(module, d, pulse) for d in destinations]
            if module == "qn":
                state = conjunction_states[module]
                for prereq, v in state.items():
                    if v == "h" and i not in prereq_seen[prereq]:
                        prereq_seen[prereq].append(i)
    periods = []
    for prereq, v in prereq_seen.items():
        periods.append(v[2] - v[1])
    ans = lcm(*periods)
    print(ans)

task1()
task2()

