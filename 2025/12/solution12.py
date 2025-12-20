from dataclasses import dataclass


@dataclass
class Tree:
    width: int
    height: int
    presents: list[int]


def parse_input(filename: str):
    with open(filename) as file:
        shapes = []
        trees = []
        for _ in range(6):
            file.readline()
            row1 = file.readline().count('#')
            row2 = file.readline().count('#')
            row3 = file.readline().count('#')
            file.readline()  # blank line
            shape = row1 + row2 + row3
            shapes.append(shape)
        for line in file.readlines():
            [size, presents] = line.split(": ")
            [width, height] = size.split("x")
            presents = [int(p) for p in presents.split(" ")]
            trees.append(Tree(int(width), int(height), presents))
    return shapes, trees


def solve(filename: str):
    data = parse_input(filename)
    (shapes, trees) = data
    result = 0
    for tree in trees:
        result += 1 if sum(
            [cnt * shape for (cnt, shape) in zip(tree.presents, shapes)]) <= tree.height * tree.width else 0

    print(result)
    return result


if __name__ == '__main__':
    # assert solve('test_input') == 2
    solve('input')
