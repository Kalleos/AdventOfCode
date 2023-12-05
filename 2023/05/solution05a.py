import re


def get_map_value(s_d_map, source_value):
    for [d, s, length] in s_d_map:
        if s <= source_value < s + length:
            return d + (source_value - s)
    return source_value


def get_location(seed, maps):
    value = int(seed)
    for my_map in maps:
        value = get_map_value(my_map, value)
    return value


def read_file(filename):
    maps = []
    new_map = {}
    with open(filename, 'r') as file:
        for line in file.read().splitlines():
            if line.startswith('seeds:'):
                seeds = re.findall('\d+', line)
                continue

            if line.endswith('map:'):
                if new_map:
                    maps.append(new_map)
                new_map = []
                continue

            ns = re.findall('\d+', line)
            if len(ns) == 3:
                new_map.append([int(n) for n in ns])
        maps.append(new_map)

    # print(seeds)
    # print(maps)

    locs = []
    for seed in seeds:
        locs.append(get_location(seed, maps))

    min_loc = min(locs)
    print(min_loc)


if __name__ == '__main__':
    read_file('test_input')
    read_file('input')
