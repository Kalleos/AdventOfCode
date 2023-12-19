import math


def read_workflow(line: str):
    rs = line.index('{')
    re = line.index('}')
    name = line[:rs]
    splitted = line[rs + 1:re].split(',')
    rules = [(rule[0], rule[1], int(rule[2:rule.index(':')]), rule[rule.index(':') + 1:]) for rule in splitted[:-1]]
    rules.append((None, None, None, splitted[-1]))

    return name, rules


def visit(workflows, wf_name, ivs):
    if wf_name == 'R':
        return 0
    if wf_name == 'A':
        return math.prod([b - a for (a, b) in ivs.values()])

    wf = workflows[wf_name]

    ivs_rest = ivs.copy()
    result = 0
    for rule in wf:
        op = rule[1]
        next_wf = rule[3]
        if op is None:
            result += visit(workflows, next_wf, ivs_rest)
            continue
        var = rule[0]
        n = rule[2]
        (a, b) = ivs_rest[var]
        if op == '<' and n > a:
            new_ivs = ivs_rest.copy()
            new_ivs[var] = (a, min(n, b))
            ivs_rest[var] = (min(n, b), b)
            result += visit(workflows, next_wf, new_ivs)

        if op == '>' and n < b:
            new_ivs = ivs_rest.copy()
            new_ivs[var] = (max(a, n) + 1, b)
            ivs_rest[var] = (a, max(a, n) + 1)
            result += visit(workflows, next_wf, new_ivs)

        if any([b - a < 1 for (a, b) in ivs_rest.values()]):
            break
    return result


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()

        workflows = {}

        for line in lines:
            if len(line) == 0:
                break
            name, rules = read_workflow(line)
            workflows[name] = rules

        ivs = {'x': (1, 4001), 'm': (1, 4001), 'a': (1, 4001), 's': (1, 4001)}
        print(visit(workflows, 'in', ivs))


if __name__ == '__main__':
    solve('test_input')
    solve('input')
