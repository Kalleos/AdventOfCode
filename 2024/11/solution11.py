lengths = {}


def blink(stone: int, times: int):
    if times == 0:
        return 1
    if (stone, times) in lengths:
        return lengths[(stone, times)]
    if stone == 0:
        length = blink(1, times - 1)
    else:
        stone_str = str(stone)
        l = len(stone_str)
        if l % 2 == 0:
            half = int(l / 2)
            left = int(stone_str[:half])
            right = int(stone_str[half:])
            length = blink(left, times - 1) + blink(right, times - 1)
        else:
            length = blink(2024 * stone, times - 1)
    lengths[(stone, times)] = length
    return length


def blink_stones(stones, times):
    result = 0
    for stone in stones:
        result += blink(stone, times)
    return result


def solve(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        stones = list(map(int, lines[0].split()))

        print(blink_stones(stones, 25))
        print(blink_stones(stones, 75))


if __name__ == '__main__':
    solve('test_input')  # 55312, 65601038650482
    solve('input')  # 185894, 221632504974231
