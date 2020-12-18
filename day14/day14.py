from pathlib import Path
from typing import Any, Dict, List, Tuple
from itertools import product

input_file: Path = Path(__file__).parent.joinpath("input.txt")


def solve(rows: List[str]) -> int:
    memory: Dict[str, int] = {}
    mask: str = ""
    for row in rows:
        if "mask" in row:
            mask = row.split("mask = ")[1]
        else:
            mem, val = row.split(" = ")
            bin_val: List[str] = list(bin(int(val)).replace("0b", "").zfill(len(mask)))
            for i, bit in enumerate(mask):
                if bit != "X":
                    bin_val[i] = bit
            memory[mem] = int("".join(bin_val), 2)

    return sum(memory.values())


def solve2(rows: List[str]) -> int:
    memory: Dict[str, int] = {}
    mask: str = ""
    for row in rows:
        if "mask" in row:
            mask = row.split("mask = ")[1]
        else:
            mem, add_val = row.split(" = ")
            val: str = mem.replace("mem[", "").replace("]", "")
            bin_val: List[str] = list(bin(int(val)).replace("0b", "").zfill(len(mask)))
            for i, bit in enumerate(mask):
                if bit != "0":
                    bin_val[i] = bit

            possible_values = list(product("01", repeat=bin_val.count("X")))
            for values in possible_values:
                mem_val: str = "".join(bin_val)
                for v in values:
                    mem_val = mem_val.replace("X", v, 1)
                memory[str(int(mem_val, 2))] = int(add_val)

    return sum(memory.values())


with open(input_file) as input:
    rows: List[str] = input.read().strip().split("\n")
    print("Solve 1:", solve(rows))
    print("Solve 2:", solve2(rows))
