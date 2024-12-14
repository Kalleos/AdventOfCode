import re
from collections import Counter

from attr import dataclass


@dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int


def get_quadrant(x, y, m, n):
    if x < int(m / 2) and y < int(n / 2):
        return 1
    if x < int(m / 2) and y > int(n / 2):
        return 2
    if x > int(m / 2) and y < int(n / 2):
        return 3
    if x > int(m / 2) and y > int(n / 2):
        return 4
    return 0


def solve(filename: str, b: int, h: int):
    with open(filename) as file:
        lines = file.read().splitlines()
        pattern = re.compile("p=(\d+),(\d+) v=(-?\d+),(-?\d+)")
        robots = []
        for line in lines:
            if m := pattern.match(line):
                robots.append(Robot(x=int(m.group(1)), y=int(m.group(2)), vx=int(m.group(3)), vy=int(m.group(4))))

        for _ in range(100):
            for robot in robots:
                robot.x = (robot.x + robot.vx) % b
                robot.y = (robot.y + robot.vy) % h

        quadrants = [get_quadrant(robot.x, robot.y, b, h) for robot in robots]
        counter = Counter(quadrants)
        result = counter[1] * counter[2] * counter[3] * counter[4]
        print(result)


if __name__ == '__main__':
    solve('test_input', 11, 7)  # 12
    solve('input', 101, 103)  # 225552000
