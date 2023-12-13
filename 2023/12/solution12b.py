cache = {}

def get_cached_arrangements(s: str, sizes: tuple[int], in_spring = False):
    if (s, sizes, in_spring) not in cache:
        cache[(s, sizes, in_spring)] = get_arrangements(s, sizes, in_spring)
    return cache.get((s, sizes, in_spring))

def get_arrangements(s: str, sizes: tuple[int], last_is_damaged = False):
    if len(s) == 0:
        return 1 if sum(sizes) == 0 else 0

    if sum(sizes) == 0:
        return 0 if '#' in s else 1

    if s[0] == '#':
        if sizes[0] == 0 and last_is_damaged:
            return 0
        return get_cached_arrangements(s[1:], (sizes[0] - 1, *sizes[1:]), True)

    if s[0] == '.':
        if last_is_damaged and sizes[0] > 0:
            return 0
        if last_is_damaged and sizes[0] == 0:
            return get_cached_arrangements(s[1:], sizes[1:], False)
        return get_cached_arrangements(s[1:], sizes, False)

    # s[0] == '?'
    if last_is_damaged and sizes[0] > 0:
        return get_cached_arrangements(s[1:], (sizes[0] - 1, *sizes[1:]), True)
    if last_is_damaged and sizes[0] == 0:
        return get_cached_arrangements(s[1:], sizes[1:], False)
    return get_cached_arrangements(s[1:], (sizes[0] - 1, *sizes[1:]), True) + get_cached_arrangements(s[1:], sizes, False)
    


def find_arrangements(line: str, n: int):
    splitted = line.split(' ')
    springs = (splitted[0] + '?') * n
    springs = springs[:-1]
    sizes = [int(n) for n in splitted[1].split(',')] * n

    #print(springs, sizes)
    return get_cached_arrangements(springs, tuple(sizes))


def solve(filename, n):
    with (open(filename) as file):
        lines = file.read().splitlines()
        result = 0
        for line in lines:
            arr = find_arrangements(line, n)
            #print(arr, line)
            result += arr
        print(result)


if __name__ == '__main__':
    solve('test_input', 1)
    solve('test_input', 5)
    solve('input', 1)
    solve('input', 5)
