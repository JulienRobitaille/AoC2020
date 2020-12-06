from pathlib import Path
from typing import List, Dict

input_file = Path(__file__).parent.joinpath("input.txt")


def empty_line(line: str) -> bool:
    return len(line) == 0


def solve1(lines: List[str]) -> List[int]:
    group_answer_count: List[int] = []
    found: List[str] = []

    for answers in lines:
        if empty_line(answers):
            group_answer_count.append(len(set(found)))
            found = []
        else:
            found = found + list(answers)

    return group_answer_count


def solve2(lines: List[str]) -> List[int]:
    group_answer_count = []
    found: Dict[str, int] = {}
    how_many_people = 0

    for answers in lines:
        if empty_line(answers):
            count = 0
            for letter in found:
                if found[letter] == how_many_people:
                    count = count + 1

            group_answer_count.append(count)
            found = {}
            how_many_people = 0
        else:
            for answer in list(answers):
                if answer in found:
                    found[answer] = found[answer] + 1
                else:
                    found[answer] = 1
            how_many_people = how_many_people + 1
    return group_answer_count


with open(input_file) as input:
    lines = input.read().split("\n")
    print("Solve 1:", sum(solve1(lines)))
    print("Solve 2:", sum(solve2(lines)))
