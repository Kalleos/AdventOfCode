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


def is_valid_game(game):
    for set in game:
        # 12 red cubes, 13 green cubes, and 14 blue cubes
        if set.get('red') > 12 or set.get('green') > 13 or set.get('blue') > 14:
            return False
    return True


with open('input', 'r') as file:
    game_nr = 0
    sum = 0
    for line in file:
        game_str = line.split(':')[1].strip()
        game = get_sets(game_str)
        print(game)
        game_nr += 1
        if is_valid_game(game):
            sum += game_nr

    print(sum) # 2528
