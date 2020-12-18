from pathlib import Path
from typing import Dict, List

input_file: Path = Path(__file__).parent.joinpath("input.txt")


def solve(numbers: List[int], max_age: int) -> int:

    last_spoken: Dict[int, List[int]] = {}
    last_number: int = 0
    for i, nb in enumerate(numbers):
        if nb not in last_spoken:
            last_spoken[nb] = [i]
        else:
            last_spoken[nb].append(i)
        last_number = nb
    for age in range(len(numbers), max_age):
        if last_number in last_spoken and len(last_spoken[last_number]) == 1:
            if 0 not in last_spoken:
                last_spoken[0] = []
            last_spoken[0].append(age)
            last_number = 0
        elif last_number in last_spoken and len(last_spoken[last_number]) > 1:
            last_index = last_spoken[last_number][-1]
            second_last_index = last_spoken[last_number][-2]
            last_number = last_index - second_last_index
            if last_number not in last_spoken:
                last_spoken[last_number] = []
            last_spoken[last_number].append(age)

    return last_number


with open(input_file) as input:
    numbers = list(map(int, input.read().strip().split(",")))
    print("Solve 1:", solve(numbers, 2020))
    print("Solve 2:", solve(numbers, 30000000))
