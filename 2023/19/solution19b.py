def read_workflow(line: str):
    rs = line.index('{')
    re = line.index('}')
    name = line[:rs]
    splitted = line[rs + 1:re].split(',')
    rules = [(rule[0], rule[1], int(rule[2:rule.index(':')]), rule[rule.index(':') + 1:]) for rule in splitted[:-1]]
    rules.append((None, None, None, splitted[-1]))

    return name, rules


def is_accepted(part, workflows):
    next_workflow = 'in'
    while next_workflow not in ['A', 'R']:
        for rule in workflows[next_workflow]:
            if isinstance(rule, str):
                next_workflow = rule
                break
            op = rule[1]
            if op == None:
                next_workflow = rule[3]
                break
            if op == '<' and part[rule[0]] < rule[2] or op == '>' and part[rule[0]] > rule[2]:
                next_workflow = rule[3]
                break
    if next_workflow == 'A':
        return True
    return False


def simplify(workflows: dict[str, list[tuple[any]] | str]):
    simplified = False
    for name in workflows:
        if isinstance(workflows[name], str):
            continue
        if all([end == 'A' for (_, _, _, end) in workflows[name]]):
            workflows[name] = 'A'
            simplified = True
            continue
        if all([end == 'R' for (_, _, _, end) in workflows[name]]):
            workflows[name] = 'R'
            simplified = True
            continue
        for i, (a, b, c, next_name) in enumerate(workflows[name]):
            if next_name not in ['A', 'R'] and isinstance(workflows[next_name], str):
                workflows[name][i] = (a, b, c, workflows[next_name])
                simplified = True
    return simplified


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()

        workflows = {}

        for line in lines:
            if len(line) == 0:
                break
            name, rules = read_workflow(line)
            workflows[name] = rules

        #print(workflows)
        for n in range(10000):
            if not simplify(workflows):
                print(f'Simplify nach {n} Runden abgeschlossen.')
                break
        #print(workflows)

        bps = {'x': [1, 4001], 'm': [1, 4001], 'a': [1, 4001], 's': [1, 4001]}
        for rules in workflows.values():
            if isinstance(rules, str):
                continue
            for rule in rules:
                op = rule[1]
                if op == '<':
                    bps[rule[0]].append(rule[2])
                if op == '>':
                    bps[rule[0]].append(rule[2] + 1)

        for c in bps:
            bps[c] = sorted(set(bps[c]))

        print(bps)
        result = 0
        for i, x in enumerate(bps['x'][:-1]):
            for j, m in enumerate(bps['m'][:-1]):
                for k, a in enumerate(bps['a'][:-1]):
                    for l, s in enumerate(bps['s'][:-1]):
                        part = {'x': x, 'm': m, 'a': a, 's': s}
                        if is_accepted(part, workflows):
                            result += (bps['x'][i + 1] - bps['x'][i]) * (bps['m'][j + 1] - bps['m'][j]) * (bps['a'][k + 1] - bps['a'][k]) * (bps['s'][l + 1] - bps['s'][l])

        print(result)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
