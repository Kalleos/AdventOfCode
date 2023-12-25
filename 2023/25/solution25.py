def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        edges = {}
        for line in lines:
            [fn, tns] = line.split(':')
            if fn not in edges:
                edges[fn] = set()
            for tn in tns.strip().split(' '):
                if tn not in edges:
                    edges[tn] = set()
                edges[fn].add(tn)
                edges[tn].add(fn)

        nodes = list(edges.keys())
        a = 0
        fn = nodes[0]
        for tn in nodes[1:]:
            used_edges = set()
            used_nodes = set()
            to_visit = [(fn, [fn])]
            path_cnt = 0
            while to_visit and path_cnt < 4:
                node, path = to_visit.pop(0)
                if node == tn:
                    path_cnt += 1
                    for k in range(len(path) - 1):
                        used_edges.add((path[k], path[k + 1]))
                    to_visit = [(fn, [fn])]
                    used_nodes = set()
                else:
                    for next_node in edges[node]:
                        if next_node not in used_nodes and (node, next_node) not in used_edges:
                            to_visit.append((next_node, path + [next_node]))
                            used_nodes.add(next_node)

            if path_cnt == 3:
                a += 1

        b = len(nodes) - a
        print(a * b)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
