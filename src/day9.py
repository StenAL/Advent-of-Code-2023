from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 9


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    all_sequences = []
    for line in data:
        line = [int(e) for e in line.split()]
        sequences = [line]
        current_sequence = line
        while not all(e == 0 for e in current_sequence):
            new_sequence = []
            for e1, e2 in zip(current_sequence, current_sequence[1:]):
                new_sequence.append(e2 - e1)
            sequences.append(new_sequence)
            current_sequence = new_sequence
        all_sequences.append(sequences)
    for sequences in all_sequences:
        sequences[-1].append(0)

    for sequences in all_sequences:
        sequences.reverse()
        for i in range(1, len(sequences)):
            sequence = sequences[i]
            sequence.append(sequences[i - 1][-1] + sequence[-1])
    ans = sum([s[-1][-1] for s in all_sequences])
    print(ans)


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    all_sequences = []
    for line in data:
        line = [int(e) for e in line.split()]
        sequences = [line]
        current_sequence = line
        while not all(e == 0 for e in current_sequence):
            new_sequence = []
            for e1, e2 in zip(current_sequence, current_sequence[1:]):
                new_sequence.append(e2 - e1)
            sequences.append(new_sequence)
            current_sequence = new_sequence
        all_sequences.append(sequences)
    for sequences in all_sequences:
        sequences[-1].insert(0, 0)

    for sequences in all_sequences:
        sequences.reverse()
        for i in range(1, len(sequences)):
            sequence = sequences[i]
            sequence.insert(0, sequence[0] - sequences[i - 1][0])

    ans = sum([s[-1][0] for s in all_sequences])
    print(ans)


task1()
task2()
