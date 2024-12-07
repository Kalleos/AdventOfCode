from functools import cmp_to_key


def correctly_ordered(update: list[int], rule: tuple[int, int]):
    if rule[0] in update and rule[1] in update:
        if update.index(rule[0]) < update.index(rule[1]):
            return True
        else:
            return False
    else:
        return True


def cmp_pages(rules: list[tuple[int, int]], page1: int, page2: int):
    for rule in rules:
        if rule == (page1, page2):
            return -1
        if rule == (page2, page1):
            return 1
    print(f"{page1} and {page2} are not comparable")
    return 0


def solve(filename: str):
    with open(filename) as file:
        blocks = file.read().split('\n\n')
        rules = [tuple(map(int, line.split('|'))) for line in blocks[0].splitlines()]
        updates = [list(map(int, line.split(','))) for line in blocks[1].splitlines()]

        # Part 1
        result = 0
        for update in updates:
            if all(correctly_ordered(update, rule) for rule in rules):
                middle = int((len(update) - 1) / 2)
                result += update[middle]
        print(result)

        # Part 2
        result = 0
        for update in updates:
            if not all(correctly_ordered(update, rule) for rule in rules):
                sorted_updated = sorted(update, key=cmp_to_key(lambda a, b: cmp_pages(rules, a, b)))
                middle = int((len(sorted_updated) - 1) / 2)
                result += sorted_updated[middle]
        print(result)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
