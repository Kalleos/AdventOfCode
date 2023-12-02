import re
from re import Pattern


def get_nr(set_str: str, pattern: Pattern):
    nrs = pattern.findall(set_str)
    return int(nrs[0]) if len(nrs) > 0 else 0


def get_set(set_str: str):
    red_pattern = re.compile(r'(\d+)\s+red')
    blue_pattern = re.compile(r'(\d+)\s+blue')
    green_pattern = re.compile(r'(\d+)\s+green')
    my_set = {
        'red': get_nr(set_str, red_pattern),
        'blue': get_nr(set_str, blue_pattern),
        'green': get_nr(set_str, green_pattern)
    }
    return my_set


def get_sets(game_str: str):
    return [get_set(set_str) for set_str in game_str.split(';')]


def get_min_set(game):
    max_red = 0
    max_green = 0
    max_blue = 0
    for set in game:
        max_red = max(max_red, set.get('red'))
        max_green = max(max_green, set.get('green'))
        max_blue = max(max_blue, set.get('blue'))
    return {
        'red': max_red,
        'blue': max_blue,
        'green': max_green
    }


def get_power(set):
    return set.get('red') * set.get('blue') * set.get('green')


with open('input', 'r') as file:
    sum = 0
    for line in file:
        game_str = line.split(':')[1].strip()
        game = get_sets(game_str)
        sum += get_power(get_min_set(game))
    print(sum)  # 67363
