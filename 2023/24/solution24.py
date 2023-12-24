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


def solve(filename, border):
    with (open(filename) as file):
        lines = file.read().splitlines()
        hailstones = [Hailstone(line) for line in lines]

        result = 0
        for i, hs1 in enumerate(hailstones):
            for j, hs2 in enumerate(hailstones):
                if i < j and (hs1.vy * hs2.vx - hs1.vx * hs2.vy) != 0:
                    t1 = ((hs2.py - hs1.py) * hs2.vx + (hs1.px - hs2.px) * hs2.vy) / (hs1.vy * hs2.vx - hs1.vx * hs2.vy)
                    t2 = (hs1.px - hs2.px + t1 * hs1.vx) / hs2.vx
                    if t1 > 0 and t2 > 0:
                        x = hs1.px + t1 * hs1.vx
                        y = hs1.py + t1 * hs1.vy
                        # print(f'will cross at x={x}, y={y}')
                        if border[0] <= x <= border[1] and border[0] <= y <= border[1]:
                            result += 1

        print(result)


if __name__ == '__main__':
    solve('test_input', (7, 27))
    solve('input', (200000000000000, 400000000000000))
