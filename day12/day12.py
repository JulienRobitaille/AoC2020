from copy import deepcopy
from pathlib import Path
from typing import Callable, List, Tuple, Dict
import math

input_file = Path(__file__).parent.joinpath("input.txt")


def east(amount: int, position: Dict[str, int]) -> None:
    position["x"] = position["x"] + amount


def west(amount: int, position: Dict[str, int]) -> None:
    position["x"] = position["x"] - amount


def north(amount: int, position: Dict[str, int]) -> None:
    position["y"] = position["y"] + amount


def south(amount: int, position: Dict[str, int]) -> None:
    position["y"] = position["y"] - amount


def move_waypoint(
    amount: int, position: Dict[str, int], waypoint: Dict[str, int]
) -> None:
    position["x"] = position["x"] + (waypoint["x"] * amount)
    position["y"] = position["y"] + (waypoint["y"] * amount)


def get_next_facing_angle(facing_angle: int, direction: str, angle: int) -> int:
    if direction == "L":
        return (facing_angle + angle) % 360
    if direction == "R":
        return (facing_angle - angle) % 360
    return 0


def rotate_coord(position: Dict[str, int], angle: float) -> Dict[str, int]:
    return {
        "x": int(
            round(position["x"] * math.cos(angle) + position["y"] * math.sin(angle))
        ),
        "y": int(
            round((-position["x"]) * math.sin(angle) + position["y"] * math.cos(angle))
        ),
    }


def solve(rows: List[str]) -> int:
    position: Dict[str, int] = {
        "x": 0,
        "y": 0,
    }
    facing_angle: int = 0
    moves: Dict[str, Callable] = {
        "E": east,
        "W": west,
        "N": north,
        "S": south,
    }
    moves_angle: Dict[str, Callable] = {
        "0": east,
        "180": west,
        "90": north,
        "270": south,
    }
    for row in rows:
        action: str = row[0]
        distance_or_angle: int = int(row[1:])

        if action == "F":
            moves_angle[str(facing_angle)](distance_or_angle, position)
        elif action == "L" or action == "R":
            facing_angle = get_next_facing_angle(
                facing_angle, action, distance_or_angle
            )

        else:
            moves[action](distance_or_angle, position)
    return abs(position["x"]) + abs(position["y"])


def solve2(rows: List[str]) -> int:
    position: Dict[str, int] = {
        "x": 0,
        "y": 0,
    }
    waypoint: Dict[str, int] = {
        "x": 10,
        "y": 1,
    }
    moves: Dict[str, Callable] = {
        "E": east,
        "W": west,
        "N": north,
        "S": south,
    }

    for row in rows:
        action: str = row[0]
        distance_or_angle: int = int(row[1:])

        if action == "F":
            move_waypoint(distance_or_angle, position, waypoint)
        elif action == "R":
            waypoint = rotate_coord(waypoint, (distance_or_angle * math.pi) / 180)
        elif action == "L":
            waypoint = rotate_coord(waypoint, -(distance_or_angle * math.pi) / 180)
        else:
            moves[action](distance_or_angle, waypoint)
    return abs(position["x"]) + abs(position["y"])


with open(input_file) as input:
    rows: List[str] = input.read().strip().split("\n")
    print("Solve 1:", solve(rows))
    print("Solve 2:", solve2(rows))
