import re


def hash_alg(s: str):
    cv = 0
    for c in s:
        cv += ord(c)
        cv *= 17
        cv %= 256
    return cv


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        result = sum([hash_alg(s) for s in lines[0].split(',')])
        print(result)

        boxes = [[] for _ in range(256)]
        steps = lines[0].split(',')  # rn=1,cm-
        r = re.compile(r'([a-z]+)([-=])(\d*)')
        for step in steps:
            m = r.match(step)
            label = m[1]
            box = boxes[hash_alg(label)]
            idx = [i for (i, (l, n)) in enumerate(box) if l == label]
            op = m[2]
            if op == '-':
                if len(idx) > 0:
                    box.pop(idx[0])
            else:
                foc = int(m[3])
                if len(idx) > 0:
                    box[idx[0]] = (label, foc)
                else:
                    box.append((label, foc))

        result = sum([sum([(i + 1) * (j + 1) * op[1] for (j, op) in enumerate(box)]) for (i, box) in enumerate(boxes)])
        print(result)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
