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


def get_seeds(line):
    seeds = []
    ns = re.findall('\d+', line)
    print(ns)
    for i in range(int(len(ns) / 2)):
        s = int(ns[2 * i])
        l = int(ns[2 * i + 1])
        seeds.append((s, l))
    return seeds


def read_file(filename):
    maps = []
    new_map = {}
    with open(filename, 'r') as file:
        for line in file.read().splitlines():
            if line.startswith('seeds:'):
                seeds = get_seeds(line)  # re.findall('\d+', line)
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

    min_loc = get_location(seeds[0][0], maps)
    for seed_range in seeds:
        for seed in range(seed_range[0], seed_range[0]+1): #seed_range[0] + seed_range[1]):
            loc = get_location(seed, maps)
            if loc < min_loc:
                min_loc = loc
                print(min_loc)

    print(min_loc)


if __name__ == '__main__':
    read_file('test_input')
    read_file('input')
