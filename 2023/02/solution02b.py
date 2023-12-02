import math

from solution02a import get_sets


def get_min_set(game):
    max_nr = {
        'red': 0,
        'blue': 0,
        'green': 0
    }
    for set in game:
        for color in set:
            max_nr[color] = max(max_nr[color], set[color])

    return max_nr


def get_power(set):
    return math.prod(set.values())


if __name__ == '__main__':
    with open('input', 'r') as file:
        sum = 0
        for line in file:
            game_str = line.split(':')[1].strip()
            game = get_sets(game_str)
            sum += get_power(get_min_set(game))
        print(sum)  # 67363
