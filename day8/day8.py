from pathlib import Path
from typing import List, Tuple

input_file = Path(__file__).parent.joinpath("input.txt")


def solve(instructions: List[str]) -> Tuple[int, int]:
    index = 0
    index_history: List[int] = []
    accumulator = 0
    while index < len(instructions) and index not in index_history:
        instruction: str = instructions[index]
        ops, _val = instruction.split(" ")
        val: int = int(_val)
        index_history.append(index)

        if ops == "nop":
            index = index + 1
        if ops == "jmp":
            index = index + val
        if ops == "acc":
            index = index + 1
            accumulator = accumulator + val
    return index, accumulator


def solve2(instructions: List[str]) -> int:
    invert = {"jmp": "nop", "nop": "jmp"}

    for index, _ in enumerate(instructions):
        instruction = instructions[index]
        ops, _ = instruction.split(" ")
        if ops in invert:
            instructions[index] = instructions[index].replace(ops, invert[ops])
            resulting_index, accumulator = solve(instructions)

            if resulting_index >= len(instructions):
                return accumulator
            else:
                instructions[index] = instruction
    return 0


with open(input_file) as input:
    instructions = input.read().strip().split("\n")
    index, acc = solve(instructions)
    print("Solve 1:", acc)
    print("Solve 2:", solve2(instructions))
