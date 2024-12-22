def parse_input(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        return list(map(int, lines))


def nth_secret_number(a: int, n: int):
    for _ in range(n):
        a = next_secret_number(a)
    return a


def mix(a: int, b: int):
    return a ^ b


def prune(a: int):
    return a % 16777216


def next_secret_number(a: int):
    a = prune(mix(a << 6, a))
    a = prune(mix(a >> 5, a))
    return prune(mix(a << 11, a))


def get_prices(a: int, n: int):
    prices = [a % 10]
    for _ in range(n):
        a = next_secret_number(a)
        prices.append(a % 10)
    return prices


def get_changes(prices: list[int]):
    changes = []
    for i in range(1, len(prices)):
        changes.append(prices[i] - prices[i - 1])
    return changes


def solve_part1(filename: str):
    secret_numbers = parse_input(filename)
    result = sum([nth_secret_number(secret_number, 2000) for secret_number in secret_numbers])
    print(result)


def solve_part2(filename: str):
    secret_numbers = parse_input(filename)

    all_prices = [get_prices(secret_number, 2000) for secret_number in secret_numbers]
    all_changes = [get_changes(prices) for prices in all_prices]

    cache = {}
    for i, changes in enumerate(all_changes):
        cache_buyer = {}
        for j in range(len(changes) - 3):
            sequence = tuple(changes[j:j + 4])
            if sequence not in cache_buyer:
                cache_buyer[sequence] = all_prices[i][j + 4]
        for key, value in cache_buyer.items():
            cache[key] = cache.get(key, 0) + value
    print(max(cache.values()))


if __name__ == '__main__':
    solve_part1('test_input')
    solve_part1('input')
    solve_part2('test_input_2')
    solve_part2('input')
