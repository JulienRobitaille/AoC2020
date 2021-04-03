from pathlib import Path
from typing import Callable, List, Optional, Union
from operator import add, mul
input_file: Path = Path(__file__).parent.joinpath("input.txt")

# 2 * (3 + 4) * 5


def parse(expression: str):
    print(expression)
    expression = expression.split()
    current = 0
    ops = None
    reserve = ""
    parenesis_count = 0
    while True:
        reserve += expression.pop(0)
        
        if reserve == "(":
            parenesis_count++
            reserve = ""
        if reserve.isnumeric():
            current = int(reserve)
            reserve = ""

    return 0

def solve(expressions: List[str]) -> int:
    total = 0
    for expression in expressions:
        #total += resolve(parse(expression))
        root = parse(expression)
    return total


with open(input_file) as input:
    expressions: List[str] = input.read().strip().split("\n")
    solve(["2 * 3 + 4 * 5"])# == 50)
    #assert(solve(["2 * 3 + (4 * 5)"]) == 26)
    #assert(solve(["5 + (8 * 3 + 9 + 3 * 4 * 3)"]) == 437)
    #assert(solve(["1 + 2 * 3 + 4 * 5 + 6"]) == 71)
    #assert(solve(["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"]) == 12240)
    #assert(solve(["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]) == 13642)
    #print("Solve 1:", solve(expressions))
    #print("Solve 2:", solve(rows))
