from pathlib import Path
from typing import List, Tuple


def solve(passwords: List[str]) -> Tuple[int, int]:
    valid_count_1 = 0
    valid_count_2 = 0

    for password in passwords:
        metadata = password.split(" ")
        start, end = map(int, metadata[0].split("-"))

        letter = metadata[1][0]
        a = metadata[2][start - 1]
        b = metadata[2][end - 1]
        amount = metadata[2].count(letter)

        if start <= amount and end >= amount:
            valid_count_1 = valid_count_1 + 1

        if (a == letter) ^ (b == letter):
            valid_count_2 = valid_count_2 + 1
    return valid_count_1, valid_count_2


input_file = Path(__file__).parent.joinpath("input.txt")

with open(input_file) as input:
    passwords = input.read().strip().split("\n")
    first, second = solve(passwords)

    print(f"Solve 1: {first}")
    print(f"Solve 2: {second}")
