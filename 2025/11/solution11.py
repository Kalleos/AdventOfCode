def parse_input(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        edges = {}
        for line in lines:
            [f, ts] = line.split(":")
            edges[f.strip()] = ts.strip().split(" ")
        return edges


def cnt_out(ways, cache, start, fft: bool, dac: bool) -> int:
    if start == 'out':
        return 1 if fft and dac else 0
    fft = fft or start == 'fft'
    dac = dac or start == 'dac'
    key = (start, fft, dac)
    if key not in cache:
        ret = 0
        if start in ways.keys():
            for next in ways[start]:
                ret += cnt_out(ways, cache, next, fft, dac)
        cache[key] = ret
    return cache[key]


def part1(filename: str):
    edges = parse_input(filename)
    to_visit = ['you']
    result = 0
    while to_visit:
        v = to_visit.pop(0)
        if v == 'out':
            result += 1
            continue
        if v in edges:
            for next in edges[v]:
                to_visit.append(next)
    print(result)
    return result


def part2(filename: str):
    edges = parse_input(filename)
    result = cnt_out(edges, {}, 'svr', False, False)
    print(result)
    return result


if __name__ == '__main__':
    assert part1('test_input') == 5
    part1('input')
    assert part2('test_input2') == 2
    part2('input')
