scores_selected = {'X': 1, 'Y': 2, 'Z': 3}
draw_comb = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]
winner_comb = [('C', 'X'), ('B', 'Z'), ('A', 'Y')]


def get_score(o, m):
    score = 0
    if (o, m) in draw_comb:
        score += 3
    if (o, m) in winner_comb:
        score += 6
    return score + scores_selected[m]


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
