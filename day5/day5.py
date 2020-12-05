from typing import List
from pathlib import Path


class PlanePartitioning:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.last_letter = ""

    def split(self, letter):
        _range = self.max - self.min
        half = _range // 2
        if letter == "F" or letter == "L":
            self.max = self.min + half
        else:
            self.min = self.max - half
        self.last_letter = letter

    def position(self):
        if self.last_letter == "F" or self.last_letter == "L":
            return min(self.min, self.max)
        elif self.last_letter == "B" or self.last_letter == "R":
            return max(self.min, self.max)


def solve(ids: List[str]) -> List[int]:
    resulting_ids: List[int] = []
    for id in ids:
        range_FB = PlanePartitioning(0, 127)
        range_LR = PlanePartitioning(0, 7)

        for letter in id[:7]:
            range_FB.split(letter)
        for letter in id[7:]:
            range_LR.split(letter)

        seat_id = (range_FB.position()) * 8 + (range_LR.position())
        resulting_ids.append(seat_id)
    return resulting_ids


input_file = Path(__file__).parent.joinpath("input.txt")

with open(input_file) as input:
    lines = input.read().strip().split("\n")

    # Example as tests
    FBFBBFFRLR, BFFFBBFRRR, FFFBBBFRRR, BBFFBBFRLL = solve(
        ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    )
    assert FBFBBFFRLR == 357
    assert BFFFBBFRRR == 567
    assert FFFBBBFRRR == 119
    assert BBFFBBFRLL == 820

    seat_ids = solve(lines)
    highest = max(seat_ids)
    print("Solve1 highest id: ", highest)

    # min .. max, e.g. 1 to 10
    complete_set = set(range(min(seat_ids), max(seat_ids)))
    difference = complete_set - set(seat_ids)

    print("Solve2 missing seat: ", difference)
