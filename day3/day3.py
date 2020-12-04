from pathlib import Path
from typing import List, Tuple


def move(xy: Tuple[int, int], slope: Tuple[int, int]) -> Tuple[int, int]:
    return (xy[0] + slope[0], xy[1] + slope[1])


def is_bottom(xy: Tuple[int, int], limit: int) -> bool:
    return xy[1] < (limit - 1)


def solve1(xy: Tuple[int, int], lines: List[str], slope: Tuple[int, int]) -> int:
    total_trees = 0
    x_amount = len(lines[0])
    y_amount = len(lines)
    while is_bottom(xy, y_amount):
        xy = move(xy, slope)
        if lines[xy[1]][xy[0] % x_amount] == "#":
            total_trees = total_trees + 1
    return total_trees


def solve2(xy: Tuple[int, int], lines: List[str], slopes: List[Tuple[int, int]]) -> int:
    total = 1
    for slope in slopes:
        total = total * solve1(xy, lines, slope)
    return total


input_file = Path(__file__).parent.joinpath("input.txt")

with open(input_file) as input:
    lines = input.read().strip().split("\n")
    slopes: List[Tuple[int, int]] = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]

    print(f"Solve 1: {solve1((0,0), lines, slopes[0])}")
    print(f"Solve 2: {solve2((0,0), lines, slopes)}")
