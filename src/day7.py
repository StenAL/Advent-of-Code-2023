from util import *
from collections import *
import copy
from functools import reduce
from math import prod
from functools import cmp_to_key

day = 7

def hand_key(hand):
    card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    card_order.reverse()
    counter = Counter(hand)
    counts = list(counter.values())
    k = 0
    if max(counts) == 5:
        k += 9 * 100000000000000
    elif max(counts) == 4:
        k += 8 * 100000000000000
    elif counts.count(2) == 1 and counts.count(3) == 1:
        k += 7 * 100000000000000
    elif max(counts) == 3:
        k += 6 * 100000000000000
    elif counts.count(2) == 2:
        k += 5 * 100000000000000
    elif counts.count(2) == 1:
        k += 4 * 100000000000000

    k += card_order.index(hand[0]) * 100000000
    k += card_order.index(hand[1]) * 1000000
    k += card_order.index(hand[2]) * 10000
    k += card_order.index(hand[3]) * 100
    k += card_order.index(hand[4]) * 1
    return k

def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    hands = []
    bids = {}
    for line in data:
        hand, bid = line.split()
        hands.append(hand)
        bids[hand] = int(bid)
    hands.sort(key=hand_key)
    ans = 0
    for i in range(len(hands)):
        ans += bids[hands[i]] * (i + 1)
    print(ans)
    

def hand_key2(hand):
    original_hand = hand
    card_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    card_order.reverse()
    counter = Counter(hand)
    counts = list(counter.values())
    if "J" in hand and counter["J"] < 5:
        del counter["J"]
        most_common_highest_card = max(counter.items(), key=lambda entry: (entry[1], card_order.index(entry[0])))
        hand = hand.replace("J", most_common_highest_card[0])
    counter = Counter(hand)
    counts = list(counter.values())
    
    k = 0
    if max(counts) == 5:
        k += 9 * 100000000000000
    elif max(counts) == 4:
        k += 8 * 100000000000000
    elif counts.count(2) == 1 and counts.count(3) == 1:
        k += 7 * 100000000000000
    elif max(counts) == 3:
        k += 6 * 100000000000000
    elif counts.count(2) == 2:
        k += 5 * 100000000000000
    elif counts.count(2) == 1:
        k += 4 * 100000000000000
    
    k += card_order.index(original_hand[0]) * 100000000
    k += card_order.index(original_hand[1]) * 1000000
    k += card_order.index(original_hand[2]) * 10000
    k += card_order.index(original_hand[3]) * 100
    k += card_order.index(original_hand[4]) * 1
    return k

def task2():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    hands = []
    bids = {}
    for line in data:
        hand, bid = line.split()
        hands.append(hand)
        bids[hand] = int(bid)
    hands.sort(key=hand_key2)
    ans = 0
    for i in range(len(hands)):
        ans += bids[hands[i]] * (i + 1)
    print(ans)
    


task1()
task2() # 253016218 too low 253907829

