from pathlib import Path
from typing import List


def solve1(lines: List[int]) -> int:
    for line1 in lines:
        for line2 in lines:
            if (line1 + line2) == 2020:
                return line1 * line2
    return 0


def solve2(lines: List[int]) -> int:
    for line1 in lines:
        for line2 in lines:
            for line3 in lines:
                if (line1 + line2 + line3) == 2020:
                    return line1 * line2 * line3
    return 0


input_file = Path(__file__).parent.joinpath("input.txt")
with open(input_file) as input:
    lines = list(map(int, input.read().strip().split("\n")))
    print(f"Solve 1: {solve1(lines)}")
    print(f"Solve 2: {solve2(lines)}")
