from copy import deepcopy
from pathlib import Path
from typing import Callable, List, Tuple
from copy import deepcopy

input_file = Path(__file__).parent.joinpath("input.txt")


def get_adjacents(rows: List[str], x: int, y: int) -> List[str]:
    return [
        rows[y - 1][x - 1],
        rows[y - 1][x],
        rows[y - 1][x + 1],
        rows[y][x - 1],
        rows[y][x + 1],
        rows[y + 1][x - 1],
        rows[y + 1][x],
        rows[y + 1][x + 1],
    ]


def raytrace(
    rows: List[str], x: int, y: int, direction_x: int, direction_y: int
) -> str:
    while True:
        x = x + direction_x
        y = y + direction_y
        candidate = rows[y][x]
        if candidate != ".":
            return candidate


def get_adjacents_raytrace(rows: List[str], x: int, y: int) -> List[str]:
    return [
        raytrace(rows, x, y, -1, -1),
        raytrace(rows, x, y, 0, -1),
        raytrace(rows, x, y, 1, -1),
        raytrace(rows, x, y, -1, 0),
        raytrace(rows, x, y, 1, 0),
        raytrace(rows, x, y, -1, 1),
        raytrace(rows, x, y, 0, 1),
        raytrace(rows, x, y, 1, 1),
    ]


def solve(
    rows: List[str],
    nb_occupied_tolerance: int = 4,
    get_adjacent_fn: Callable[[List[str], int, int], List[str]] = get_adjacents,
) -> int:
    # Pad the matrix
    y_len: int = len(rows)
    x_len: int = len(rows[0])
    rows = ["-" * x_len] + rows + ["-" * x_len]
    for i, row in enumerate(rows):
        rows[i] = "-" + row + "-"

    limit: int = 100
    while limit >= 0:
        mutations: List[Tuple[int, int, str]] = []
        for y in range(y_len):
            for x in range(x_len):
                adjacents: List[str] = get_adjacent_fn(rows, x + 1, y + 1)
                current = rows[y + 1][x + 1]

                nb_occupied: int = "".join(adjacents).count("#")
                if current == "L" and nb_occupied == 0:
                    mutations.append((y + 1, x + 1, "#"))
                elif current == "#" and nb_occupied >= nb_occupied_tolerance:
                    mutations.append((y + 1, x + 1, "L"))

        # Update from mutation
        for y, x, result in mutations:
            mutation_row: List[str] = list(rows[y])
            mutation_row[x] = result
            rows[y] = "".join(mutation_row)

        # Stop
        if not mutations:
            occ = 0
            for row in rows:
                occ = occ + row.count("#")
            return occ

        limit = limit - 1
    return 0


with open(input_file) as input:
    rows = input.read().strip().split("\n")
    print("Solve 1:", solve(rows))
    print("Solve 2:", solve(rows, 5, get_adjacents_raytrace))
