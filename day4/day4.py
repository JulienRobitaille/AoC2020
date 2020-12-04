from typing import Dict, Callable, List
from pathlib import Path
import re


def validate_hcl(value: str) -> bool:
    return re.match("^#[0-9a-f]{6}$", value) != None


def validate_ecl(value: str) -> bool:
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_pid(value: str) -> bool:
    return value.isnumeric() and len(value) == 9


def validate_byr(value: str) -> bool:
    return len(value) == 4 and int(value) >= 1920 and int(value) <= 2002


def validate_iyr(value: str) -> bool:
    return len(value) == 4 and int(value) >= 2010 and int(value) <= 2020


def validate_eyr(value: str) -> bool:
    return len(value) == 4 and int(value) >= 2020 and int(value) <= 2030


def validate_hgt(value: str) -> bool:
    if "cm" in value:
        return validate_hgt_cm(value.replace("cm", ""))
    elif "in" in value:
        return validate_hgt_in(value.replace("in", ""))
    else:
        return False


def validate_hgt_cm(value: str) -> bool:
    return value.isnumeric() and int(value) >= 150 and int(value) <= 193


def validate_hgt_in(value: str) -> bool:
    return value.isnumeric() and int(value) >= 59 and int(value) <= 76


# Simple tests
assert validate_byr("2002")
assert not validate_byr("2003")

assert validate_hgt("60in")
assert validate_hgt("190cm")
assert not validate_hgt("190in")
assert not validate_hgt("190")

assert validate_hcl("#123abc")
assert not validate_hcl("#123aBc")
assert not validate_hcl("#123abz")
assert not validate_hcl("123abc")

assert validate_ecl("brn")
assert not validate_ecl("wat")

assert validate_pid("000000001")
assert not validate_pid("0123456789")


def passport_fields_with_validator() -> Dict[str, Callable]:
    return {
        "byr": validate_byr,
        "iyr": validate_iyr,
        "eyr": validate_eyr,
        "hgt": validate_hgt,
        "hcl": validate_hcl,
        "ecl": validate_ecl,
        "pid": validate_pid,
    }


def empty_line(line: str) -> bool:
    return len(line) == 0


def solve(lines: List[str], solve2: bool = False) -> int:
    validate_count = 0
    field_validators = passport_fields_with_validator()

    # Passpost data can be on multiple lines
    for line in lines:
        if empty_line(line):
            # When field_validators is empty it means that all the field were found and are valid
            if len(field_validators) == 0:
                validate_count = validate_count + 1
            field_validators = passport_fields_with_validator()
            continue

        fields = line.split(" ")
        for field in fields:
            id, val = field.split(":")

            # If the field exist and it is valid, we remove it from the dict
            if id in field_validators and (not solve2 or field_validators[id](val)):
                del field_validators[id]
    return validate_count


input_file = Path(__file__).parent.joinpath("input.txt")

with open(input_file) as input:
    lines = input.read().split("\n")
    print("Solve first:", solve(lines))
    print("Solve second:", solve(lines, True))
