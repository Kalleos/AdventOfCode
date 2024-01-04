from __future__ import annotations


class Position:

    def __init__(self, x: str, y: str, z: str):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __repr__(self):
        return f'{self.x},{self.y},{self.z}'

    def fall(self):
        self.z = self.z - 1


class Brick:

    def __init__(self, begin: Position, end: Position):
        assert begin.z <= end.z
        self.begin = begin
        self.end = end
        self.support_for = []
        self.supported_by = []
        self.cnt_let_fall = -1

    def __repr__(self):
        return f'{self.begin} - {self.end}'

    def fall(self):
        self.begin.fall()
        self.end.fall()

    def supports(self, other: Brick) -> bool:
        return self.end.z == other.begin.z - 1 and max(self.begin.x, other.begin.x) <= min(self.end.x,
                                                                                           other.end.x) and max(
            self.begin.y, other.begin.y) <= min(self.end.y, other.end.y)


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        bricks = []
        for line in lines:
            b, e = line.split('~')
            bricks.append(Brick(Position(*b.split(',')), Position(*e.split(','))))

        # print(bricks)

        bricks.sort(key=lambda b: b.begin.z)
        for i, brick in enumerate(bricks):
            is_supported = brick.begin.z == 1
            while not is_supported and brick.begin.z > 1:
                for lower_brick in bricks[0:i]:
                    if lower_brick.supports(brick):
                        is_supported = True
                        lower_brick.support_for.append(brick)
                        brick.supported_by.append(lower_brick)
                if not is_supported:
                    brick.fall()

        result_1 = 0
        for i, brick in enumerate(bricks):
            if not brick.support_for or all(len(other_brick.supported_by) > 1 for other_brick in brick.support_for):
                # print(f'Brick {i} can be disintegrated')
                result_1 += 1
        print(result_1)

        result_2 = 0
        for i, brick in enumerate(bricks):
            falling_bricks = [brick]
            k = 0
            while k < len(falling_bricks):
                cb = falling_bricks[k]
                for sb in cb.support_for:
                    if sb not in falling_bricks and len(
                            [item for item in sb.supported_by if item not in falling_bricks]) == 0:
                        falling_bricks.append(sb)
                k += 1
            # print(f'Brick {i} let {len(falling_bricks) - 1} other bricks to fall')
            result_2 += len(falling_bricks) - 1
        print(result_2)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
