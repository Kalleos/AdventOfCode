def solve(filename):
    with (open(filename) as file):
        elves = file.read().split('\n\n')
        sums = []
        for elf in elves:
            sums.append(sum([int(line) for line in elf.splitlines()]))
        reversed_sum = sorted(sums, reverse=True)

        print(reversed_sum[0])
        print(sum(reversed_sum[0: 3]))


if __name__ == '__main__':
    solve('test_input')
    solve('input')