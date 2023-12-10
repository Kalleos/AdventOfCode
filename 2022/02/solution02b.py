scores_selected = {'A': 1, 'B': 2, 'C': 3}
draw_comb = [('A', 'A'), ('B', 'B'), ('C', 'C')]
winner_comb = [('C', 'A'), ('B', 'C'), ('A', 'B')]


def get_score(o, m):
    selected = ''
    if m == 'Y': # draw
        selected = o
    if m == 'X': # loose
        selected = [comb[0] for comb in winner_comb if comb[1] == o][0]
    if m == 'Z': # loose
        selected = [comb[1] for comb in winner_comb if comb[0] == o][0]

    score = 0
    if (o, selected) in draw_comb:
        score += 3
    if (o, selected) in winner_comb:
        score += 6
    return score + scores_selected[selected]


def solve(filename):
    with (open(filename) as file):
        line = file.read().splitlines()
        result = 0
        for l in line:
            o, m = l.split(' ')
            result += get_score(o, m)
        print(result)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
