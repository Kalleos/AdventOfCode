import re
from itertools import chain


def get_map_value(s_d_map, source_value):
    for [d, s, length] in s_d_map:
        if s <= source_value < s + length:
            return d + (source_value - s)
    return source_value


def get_reverse_map_value(s_d_map, dest_value):
    for [d, s, length] in s_d_map:
        if d <= dest_value < d + length:
            return s + (dest_value - d)
    return dest_value


def get_location(seed, maps):
    value = int(seed)
    for my_map in maps:
        value = get_map_value(my_map, value)
    return value


def get_seeds(line):
    seeds = []
    ns = re.findall(r'\d+', line)
    for i in range(int(len(ns) / 2)):
        s = int(ns[2 * i])
        l = int(ns[2 * i + 1])
        seeds.append((s, l))
    return seeds


def flatten(matrix):
    return list(chain.from_iterable(matrix))


def is_in_seed_intervals(seed_intervals, value):
    for (s, l) in seed_intervals:
        if s <= value < s + l:
            return True
    return False


def read_file(filename):
    maps = []
    new_map = {}
    with open(filename, 'r') as file:
        for line in file.read().splitlines():
            if line.startswith('seeds:'):
                seed_intervals = get_seeds(line)
                continue

            if line.endswith('map:'):
                if new_map:
                    maps.append(new_map)
                new_map = []
                continue

            ns = re.findall(r'\d+', line)
            if len(ns) == 3:
                new_map.append([int(n) for n in ns])
        maps.append(new_map)

    maps.reverse()
    limits = []
    for my_map in maps:
        limits.extend(flatten([[d, d + length - 1] for [d, _, length] in my_map]))
        limits = [get_reverse_map_value(my_map, limit) for limit in limits]

    relevant_limits = [value for value in limits if is_in_seed_intervals(seed_intervals, value)]
    seeds = flatten([[s, s + l - 1] for (s, l) in seed_intervals]) + relevant_limits

    maps.reverse()
    min_loc = get_location(seeds[0], maps)
    for seed in seeds:
        loc = get_location(seed, maps)
        if loc < min_loc:
            min_loc = loc

    print(min_loc)


if __name__ == '__main__':
    read_file('test_input')
    read_file('input')
