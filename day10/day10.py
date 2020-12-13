from pathlib import Path
from typing import List

input_file = Path(__file__).parent.joinpath("input.txt")


def solve(joltages: List[int]) -> int:
    adapter_capacity: int = max(joltages) + 3
    joltages = list(sorted(joltages))
    joltages.append(adapter_capacity)

    current_adapter_joltage: int = 0
    amount_one: int = 0
    amount_three: int = 0

    for joltage in joltages:
        if (joltage - 1) == current_adapter_joltage:
            amount_one = amount_one + 1
        if (joltage - 3) == current_adapter_joltage:
            amount_three = amount_three + 1
        current_adapter_joltage = joltage

    return amount_one * amount_three


class Tree:
    def __init__(self, joltage, joltages):
        self._joltage = joltage
        self._joltages = joltages

    def walk(self, memo={}) -> int:
        if self._joltage == max(self._joltages):
            return 1
        result = 0
        for i in range(1, 4):
            if (
                f"{self._joltage}_{i}" not in memo
                and (self._joltage + i) in self._joltages
            ):
                next = Tree(self._joltage + i, self._joltages)
                child_result = next.walk(memo)
                memo[f"{self._joltage}_{i}"] = child_result

            if f"{self._joltage}_{i}" in memo:
                result = result + memo[f"{self._joltage}_{i}"]

        return result


def solve2(joltages: List[int]) -> int:
    adapter_capacity: int = max(joltages) + 3
    joltages = list(sorted(joltages))
    joltages.append(adapter_capacity)
    total_distinct_arrangements: int = Tree(0, joltages).walk()
    return total_distinct_arrangements


with open(input_file) as input:
    joltages: List[int] = list(map(int, input.read().strip().split("\n")))
    print("Solve 1:", solve(joltages))
    print("Solve 2:", solve2(joltages))
