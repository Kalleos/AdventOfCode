import sympy


class Hailstone:

    def __init__(self, line: str):
        [pos, velo] = line.split('@')
        [pxs, pys, pzs] = pos.strip().split(',')
        self.px = int(pxs.strip())
        self.py = int(pys.strip())
        self.pz = int(pzs.strip())

        [vxs, vys, vzs] = velo.strip().split(',')
        self.vx = int(vxs.strip())
        self.vy = int(vys.strip())
        self.vz = int(vzs.strip())

    def __repr__(self):
        return f'{self.px}, {self.py}, {self.pz}'


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        hailstones = [Hailstone(line) for line in lines]

        x, y, z, u, v, w = sympy.symbols("x, y, z, u, v, w")
        eqs = []

        for hs in hailstones:
            eqs.append((hs.px - x) / (u - hs.vx) - (hs.py - y) / (v - hs.vy))
            eqs.append((hs.px - x) / (u - hs.vx) - (hs.pz - z) / (w - hs.vz))

        for solution in sympy.solve(eqs):
            print(solution)
            print(solution[x] + solution[y] + solution[z])


if __name__ == '__main__':
    solve('test_input')
    solve('input')
