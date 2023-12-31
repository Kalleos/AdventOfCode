import itertools

card_rank = list(reversed('A,K,Q,J,T,9,8,7,6,5,4,3,2'.split(',')))


def get_type_pattern(hand):
    return ''.join(sorted([str(len(list(g))) for k, g in itertools.groupby(sorted(hand))], reverse=True))


def get_valued_hand(hand):
    return [card_rank.index(card) for card in hand]


def solve(filename):
    with open(filename, 'r') as f:
        cards_lines = [line.split(' ') for line in f.read().splitlines()]
        hands = [(hand, int(bit)) for [hand, bit] in cards_lines]
        hands_sorted = sorted(hands, key=lambda hand: [get_type_pattern(hand[0])] + get_valued_hand(hand[0]))
        result = 0
        for idx, (hand, bit) in enumerate(hands_sorted):
            result += (idx + 1) * bit
        print(result)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
