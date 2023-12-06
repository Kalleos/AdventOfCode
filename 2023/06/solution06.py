import re


def get_beat_of_race(time, distance):
    return sum([(time - t) * t > distance for t in range(time)])


def solve(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        ts = re.findall(r'\d+', lines[0])
        ds = re.findall(r'\d+', lines[1])

        prod = 1
        for i in range(len(ts)):
            prod *= get_beat_of_race(int(ts[i]), int(ds[i]))
        print(prod)


if __name__ == '__main__':
    solve('test_input')
    solve('input')

    print(get_beat_of_race(71530, 940200))
    print(get_beat_of_race(63789468, 411127420471035))
