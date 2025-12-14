def parse_input(filename: str):
    with open(filename) as file:
        s = file.read()
        [ranges_s, ingredients_s] = s.split("\n\n")

        ranges = [[int(n) for n in line.split("-")] for line in ranges_s.split("\n")]
        ingredients = [int(n) for n in ingredients_s.split("\n")]
    return ranges, ingredients


def part1(filename: str):
    ranges, ingredients = parse_input(filename)
    result = sum([any(start <= i <= end for [start, end] in ranges) for i in ingredients])
    print(result)
    return result


def part2(filename: str):
    ranges, _ = parse_input(filename)
    ranges.sort()
    merged = [ranges[0]]
    for r in ranges[1:]:
        if r[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], r[1])
        else:
            merged.append(r)
    result = sum(end - start + 1 for start, end in merged)
    print(result)
    return result


if __name__ == '__main__':
    assert part1('test_input') == 3
    part1('input')
    assert part2('test_input') == 14
    part2('input')
