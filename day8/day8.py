from pathlib import Path
from typing import List, final
from copy import copy

input_file = Path(__file__).parent.joinpath("input.txt")


def solve(instructions: List[str]):
    accumulator = 0
    index = 0
    instruction = instructions[index]
    runned_instruction = []
    try:
        while index not in runned_instruction:
            runned_instruction.append(index)

            ops, _val = instruction.split(" ")
            val = int(_val)

            if ops == "nop":
                index = index + 1
            if ops == "jmp":
                index = index + val
            if ops == "acc":
                index = index + 1
                accumulator = accumulator + val

            instruction = instructions[index]
    except:
        raise Exception(accumulator)

    return accumulator


def solve2(instructions: List[str]):
    invert = {"jmp": "nop", "nop": "jmp"}
    for i, instruction in enumerate(instructions):
        ops, _ = instruction.split(" ")
        instructions_candidate = copy(instructions)
        try:
            if ops == "nop" or ops == "jmp":
                instructions_candidate[i] = instruction.replace(ops, invert[ops])
                _ = solve(instructions_candidate)
        except Exception as err:
            return err  # This is an ugly hack


with open(input_file) as input:
    instructions = input.read().strip().split("\n")
    print("Solve 1:", solve(instructions))
    print("Solve 1:", solve2(instructions))
