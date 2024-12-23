import networkx as nx


def parse_input(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        return [tuple(line.split('-')) for line in lines]


def starts_with_t(t):
    return any(c.startswith('t') for c in t)


def solve(filename: str):
    connections = parse_input(filename)

    G = nx.Graph()
    G.add_edges_from(connections)

    lan_parties = set()
    max_length = 0
    max_clique = []
    for clique in nx.enumerate_all_cliques(G):
        if len(clique) == 3:
            lan_parties.add(tuple(sorted(clique)))
        if len(clique) > max_length:
            max_clique = clique
            max_length = len(clique)
    print(sum(map(starts_with_t, lan_parties)))

    print(','.join(sorted(max_clique)))


if __name__ == '__main__':
    solve('test_input')
    solve('input')
