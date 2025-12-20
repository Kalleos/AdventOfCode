import math
from collections import Counter


def parse_input(filename: str) -> list[tuple[int, int, int]]:
    with open(filename) as file:
        lines = file.read().splitlines()
        boxes = [tuple(int(c) for c in line.split(",")) for line in lines]
        return boxes


def distance(box1: tuple[int, int, int], box2: tuple[int, int, int]) -> float:
    (x1, y1, z1) = box1
    (x2, y2, z2) = box2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def solve(filename: str, n: int):
    boxes = parse_input(filename)
    dists = {}
    circuits = {i: i for i in range(len(boxes))}
    for i in range(len(boxes)):
        for j in range(i):
            dists[(i, j)] = distance(boxes[i], boxes[j])
    dists = dict(sorted(dists.items(), key=lambda item: item[1]))

    for (i, j) in list(dists.keys())[0:n]:
        new_circuit = min(circuits[i], circuits[j])
        old_circuit = max(circuits[i], circuits[j])
        for k in range(len(boxes)):
            if circuits[k] == old_circuit:
                circuits[k] = new_circuit

    cnt = Counter(circuits.values())
    result = math.prod([c[1] for c in cnt.most_common(3)[0:3]])

    print(result)
    return result


def solve2(filename: str):
    result = 0
    boxes = parse_input(filename)
    dists = {}
    circuits = {i: i for i in range(len(boxes))}
    for i in range(len(boxes)):
        for j in range(i):
            dists[(i, j)] = distance(boxes[i], boxes[j])
    dists = dict(sorted(dists.items(), key=lambda item: item[1]))

    for (i, j) in dists.keys():
        new_circuit = min(circuits[i], circuits[j])
        old_circuit = max(circuits[i], circuits[j])
        for k in range(len(boxes)):
            if circuits[k] == old_circuit:
                circuits[k] = new_circuit
        if all(val == 0 for val in circuits.values()):
            result = boxes[i][0] * boxes[j][0]
            break

    print(result)
    return result


if __name__ == '__main__':
    assert solve('test_input', 10) == 40
    assert solve('input', 1000) == 97384
    assert solve2('test_input') == 25272
    assert solve2('input') == 9003685096
