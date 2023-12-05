from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 5

def get_match(original, ingredient_map):
    match = None
    for dest, source, l in ingredient_map:
        if 0 <= (original - source) < l:
            match = dest + (original - source)
    if not match:
        match = original
    return match

def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")

    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []
    parse_mode = "seeds"
    for line in data:
        if line == "":
            if parse_mode == "seeds":
                parse_mode = "s-to-s"
            elif parse_mode == "s-to-s":
                parse_mode = "s-to-f"
            elif parse_mode == "s-to-f":
                parse_mode = "f-to-w"
            elif parse_mode == "f-to-w":
                parse_mode = "w-to-l"
            elif parse_mode == "w-to-l":
                parse_mode = "l-to-t"
            elif parse_mode == "l-to-t":
                parse_mode = "t-to-h"
            elif parse_mode == "t-to-h":
                parse_mode = "h-to-l"
            continue
        if parse_mode == "seeds":
            seeds = [int(n) for n in line.split(": ")[1].split()]
        elif parse_mode == "s-to-s" and "seed-to-soil map" not in line:
            seed_to_soil.append(tuple(int(n) for n in line.split()))
        elif parse_mode == "s-to-f" and "soil-to-fertilizer map" not in line:
            soil_to_fertilizer.append(tuple(int(n) for n in line.split()))
        elif parse_mode == "f-to-w" and "fertilizer-to-water map" not in line:
            fertilizer_to_water.append(tuple(int(n) for n in line.split()))
        elif parse_mode == "w-to-l" and "water-to-light map" not in line:
            water_to_light.append(tuple(int(n) for n in line.split()))
        elif parse_mode == "l-to-t" and "light-to-temperature map" not in line:
            light_to_temperature.append(tuple(int(n) for n in line.split()))
        elif parse_mode == "t-to-h" and "temperature-to-humidity map" not in line:
            temperature_to_humidity.append(tuple(int(n) for n in line.split()))
        elif parse_mode == "h-to-l" and "humidity-to-location map" not in line:
            humidity_to_location.append(tuple(int(n) for n in line.split()))
    locations = []
    for seed in seeds:
        soil = get_match(seed, seed_to_soil)
        fertilizer = get_match(soil, soil_to_fertilizer)
        water = get_match(fertilizer, fertilizer_to_water)
        light = get_match(water, water_to_light)
        temperature = get_match(light, light_to_temperature)
        humidity = get_match(temperature, temperature_to_humidity)
        location = get_match(humidity, humidity_to_location)
        locations.append(location)
    ans = min(locations)
    print(ans)


def task2():
    data = get_input_for_day(day)
    data = get_input_for_file("test")

    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []
    parse_mode = "seeds"
    for line in data:
        if "map" in line:
            continue
        if line == "":
            if parse_mode == "seeds":
                parse_mode = "s-to-s"
            elif parse_mode == "s-to-s":
                parse_mode = "s-to-f"
            elif parse_mode == "s-to-f":
                parse_mode = "f-to-w"
            elif parse_mode == "f-to-w":
                parse_mode = "w-to-l"
            elif parse_mode == "w-to-l":
                parse_mode = "l-to-t"
            elif parse_mode == "l-to-t":
                parse_mode = "t-to-h"
            elif parse_mode == "t-to-h":
                parse_mode = "h-to-l"
            continue
        if parse_mode == "seeds":
            seeds = [int(n) for n in line.split(": ")[1].split()]
            seed_ranges = []
            for i in range(0, len(seeds), 2):
                seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1] -1, 0)) # start, end, transformation stage
            seeds = seed_ranges
        else:
            dest, src, l = [int(n) for n in line.split()]
            l -= 1
            if parse_mode == "s-to-s":
                seed_to_soil.append(((src, src + l), (dest, dest + l)))
            elif parse_mode == "s-to-f":
                soil_to_fertilizer.append(((src, src + l), (dest, dest + l)))
            elif parse_mode == "f-to-w":
                fertilizer_to_water.append(((src, src + l), (dest, dest + l)))
            elif parse_mode == "w-to-l":
                water_to_light.append(((src, src + l), (dest, dest + l)))
            elif parse_mode == "l-to-t":
                light_to_temperature.append(((src, src + l), (dest, dest + l)))
            elif parse_mode == "t-to-h":
                temperature_to_humidity.append(((src, src + l), (dest, dest + l)))
            elif parse_mode == "h-to-l":
                humidity_to_location.append(((src, src + l), (dest, dest + l)))
    maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]
    print(seed_to_soil)
    locations = []
    q = seeds
    while len(q) > 0:
        start, end, stage = q.pop(0)
        found_match = False

        if stage == len(maps):
            locations.append((start, end))
            continue
        for (src_start, src_end), (dst_start, dst_end) in maps[stage]:
            if src_start <= start <= src_end:
                offset = start - src_start
                overlap_start = start
                overlap_end = min(end, src_end)
                new_start = dst_start + offset
                new_end = new_start + (overlap_end - overlap_start)
                q.append((new_start, new_end, stage + 1))
                #print(f"stage {stage}, {(start, end)} -> {(new_start, new_end)} (rule {(src_start, src_end)} -> {(dst_start, dst_end)})")
                if end > src_end:
                    #print(f"stage {stage}, {(start, end)} -> {(src_end + 1, end)} (reprocess)")
                    q.append((src_end + 1, end, stage))
                found_match = True
        if not found_match:
            #print(f"stage {stage}, {(start, end)} -> skip")
            q.append((start, end, stage + 1))
    ans = min(min(l) for l in locations)
    print(ans)

task1()
task2()
