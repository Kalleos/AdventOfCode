import re

import numpy as np
from PIL import Image
from attr import dataclass


@dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int


def draw(robots: list[Robot], w: int, h: int, k: int):
    data = np.zeros((h, w, 3), dtype=np.uint8)
    for robot in robots:
        data[robot.y][robot.x] = [255, 255, 255]
    img = Image.fromarray(data, 'RGB')
    img.save(f"{k}.png")


def sparsity(robots: list[Robot]):
    center_x = int(sum([robot.x for robot in robots]) / len(robots))
    center_y = int(sum([robot.y for robot in robots]) / len(robots))
    return sum([abs(center_x - robot.x) for robot in robots]) + sum([abs(center_y - robot.y) for robot in robots])


def solve(filename: str, b: int, h: int):
    with open(filename) as file:
        lines = file.read().splitlines()
        pattern = re.compile("p=(\d+),(\d+) v=(-?\d+),(-?\d+)")
        robots = []
        for line in lines:
            if m := pattern.match(line):
                robots.append(Robot(x=int(m.group(1)), y=int(m.group(2)), vx=int(m.group(3)), vy=int(m.group(4))))

        min_sparsity = float('inf')
        k = 0
        for step in range(1, 10000):
            for robot in robots:
                robot.x = (robot.x + robot.vx) % b
                robot.y = (robot.y + robot.vy) % h
            current_sparsity = sparsity(robots)
            if current_sparsity < min_sparsity:
                draw(robots, b, h, step)
                min_sparsity = current_sparsity
                k = step
        print(k)


if __name__ == '__main__':
    solve('input', 101, 103)
