import itertools

card_rank = 'A,K,Q,J,T,9,8,7,6,5,4,3,2'.split(',')


def get_type_pattern(card):
    return ''.join(sorted([str(len(list(g))) for k, g in itertools.groupby(sorted(card))], reverse=True))


def solve(filename):
    with open(filename, 'r') as f:
        cards_lines = [line.split(' ') for line in f.read().splitlines()]
        cards = [(card, int(bit)) for [card, bit] in cards_lines]
        for card in cards:
            print(card, get_type_pattern(card[0]))




if __name__ == '__main__':
    solve('test_input')
