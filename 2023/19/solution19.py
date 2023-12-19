def read_workflow(line: str):
    rs = line.index('{')
    re = line.index('}')
    name = line[:rs]
    splitted = line[rs + 1:re].split(',')
    rules = [(rule[0], rule[1], int(rule[2:rule.index(':')]), rule[rule.index(':') + 1:]) for rule in splitted[:-1]]
    rules.append((splitted[-1], None, None, None))

    return name, rules


def read_part(line: str):
    return dict([(var[0], int(var[2:])) for var in line[1:-1].split(',')])


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()

        workflows = {}
        parts = []

        reading_workflows = True
        for line in lines:
            if len(line) == 0:
                reading_workflows = False
                continue
            if reading_workflows:
                name, rules = read_workflow(line)
                workflows[name] = rules
            else:
                parts.append(read_part(line))

        result = 0
        for part in parts:
            next_workflow = 'in'
            while next_workflow not in ['A', 'R']:
                for rule in workflows[next_workflow]:
                    op = rule[1]
                    if op == None:
                        next_workflow = rule[0]
                        break
                    if op == '<' and part[rule[0]] < rule[2] or op == '>' and part[rule[0]] > rule[2]:
                        next_workflow = rule[3]
                        break
            if next_workflow == 'A':
                result += sum(part.values())

        print(result)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
