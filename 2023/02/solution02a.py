import re


def get_set(set_str: str):
    # 1 red, 4 blue, 2 green
    pattern = re.compile(r'(\d+)\s+([a-z]+)')
    cubes = pattern.findall(set_str)
    return dict([(color, int(nr)) for (nr, color) in cubes])


def get_sets(game_str: str):
    return [get_set(set_str) for set_str in game_str.split(';')]


def is_valid_game(game):
    for set in game:
        # 12 red cubes, 13 green cubes, and 14 blue cubes
        if 'red' in set and set['red'] > 12 \
                or 'green' in set and set['green'] > 13 \
                or 'blue' in set and set['blue'] > 14:
            return False
    return True


if __name__ == '__main__':
    with open('input', 'r') as file:
        sum = 0
        for line in file:
            game_nr = int(re.findall(r'^Game (\d+):', line)[0])
            game_str = line.split(':')[1].strip()
            game = get_sets(game_str)
            if is_valid_game(game):
                sum += game_nr

        print(sum)  # 2528
