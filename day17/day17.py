from pathlib import Path
from typing import Dict, List
from copy import deepcopy


def get_neighbor_states_hypercube(
    cube_addr: str, positions: Dict[str, bool]
) -> List[bool]:
    states: List[bool] = []
    x, y, z, w = list(map(int, cube_addr.split("|")))
    for _w in range(w - 1, w + 2):
        for _z in range(z - 1, z + 2):
            for _y in range(y - 1, y + 2):
                for _x in range(x - 1, x + 2):
                    cube_neighbor_addr: str = f"{_x}|{_y}|{_z}|{_w}"
                    if cube_addr != cube_neighbor_addr:
                        if (
                            cube_neighbor_addr in positions
                            and positions[cube_neighbor_addr]
                        ):
                            states.append(positions[cube_neighbor_addr])
    return states


def get_neighbor_states(cube_addr: str, positions: Dict[str, bool]) -> List[bool]:
    states: List[bool] = []
    x, y, z = list(map(int, cube_addr.split("|")))
    for _z in range(z - 1, z + 2):
        for _y in range(y - 1, y + 2):
            for _x in range(x - 1, x + 2):
                cube_neighbor_addr: str = f"{_x}|{_y}|{_z}"
                if cube_addr != cube_neighbor_addr:
                    if (
                        cube_neighbor_addr in positions
                        and positions[cube_neighbor_addr]
                    ):
                        states.append(positions[cube_neighbor_addr])
    return states


def cube_walk_hypercube(positions: Dict[str, bool]) -> Dict[str, bool]:
    new_pos: Dict[str, bool] = deepcopy(positions)
    for w in range(-20, 20):
        for z in range(-20, 20):
            for y in range(-20, 20):
                for x in range(-20, 20):
                    cube_addr: str = f"{x}|{y}|{z}|{w}"
                    nb_active: int = sum(
                        get_neighbor_states_hypercube(cube_addr, positions)
                    )

                    if cube_addr in positions:
                        new_pos[cube_addr] = False
                        if positions[cube_addr] and nb_active in [2, 3]:
                            new_pos[cube_addr] = True
                        if not positions[cube_addr] and nb_active == 3:
                            new_pos[cube_addr] = True
                    else:
                        if nb_active == 3:
                            new_pos[cube_addr] = True
    return new_pos


def cube_walk(positions: Dict[str, bool]) -> Dict[str, bool]:
    new_pos: Dict[str, bool] = deepcopy(positions)
    for z in range(-20, 20):
        for y in range(-20, 20):
            for x in range(-20, 20):
                cube_addr: str = f"{x}|{y}|{z}"
                nb_active: int = sum(get_neighbor_states(cube_addr, positions))

                if cube_addr in positions:
                    new_pos[cube_addr] = False
                    if positions[cube_addr] and nb_active in [2, 3]:
                        new_pos[cube_addr] = True
                    if not positions[cube_addr] and nb_active == 3:
                        new_pos[cube_addr] = True
                else:
                    if nb_active == 3:
                        new_pos[cube_addr] = True
    return new_pos


input_file: Path = Path(__file__).parent.joinpath("input.txt")


def solve(rows: List[str], hypercube: bool = False) -> int:
    positions: Dict[str, bool] = {}

    for y, row in enumerate(rows):
        for x, letter in enumerate(list(row)):
            if hypercube:
                positions[f"{x}|{y}|0|0"] = letter == "#"
            else:
                positions[f"{x}|{y}|0"] = letter == "#"

    for i in range(0, 6):
        if hypercube:
            positions = cube_walk_hypercube(positions)
        else:
            positions = cube_walk(positions)
    return sum(filter(lambda v: v, positions.values()))


with open(input_file) as input:
    rows: List[str] = input.read().strip().split("\n")
    print("Solve 1:", solve(rows))
    print("Solve 2:", solve(rows, hypercube=True))
