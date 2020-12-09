from pathlib import Path
from typing import List

input_file = Path(__file__).parent.joinpath("input.txt")


def two_number_can_sum(target: int, list: List[int]) -> bool:
    for nb1 in list:
        for nb2 in list:
            if (nb1 + nb2) == target:
                return True
    return False


def solve(lines: List[int], preamble: int) -> int:
    for i, value in enumerate(lines):
        if i < preamble:
            continue
        if not two_number_can_sum(value, lines[i - preamble : i + preamble]):
            return value
    return 0


def solve2(lines: List[int], target: int) -> int:
    for start in range(0, len(lines)):
        for i in range(0, len(lines)):
            end = start + i + 1
            if end < len(lines):
                _range = lines[start : end + 1]
                total = sum(_range)
                if total == target:
                    return min(_range) + max(_range)
                if total > target:
                    break
    return 0


with open(input_file) as input:
    lines = list(map(int, input.read().strip().split("\n")))
    target = solve(lines, 25)
    print("Solve 1:", target)
    print("Solve 2:", solve2(lines, target))
