from pathlib import Path
from typing import Callable, Dict, List

input_file: Path = Path(__file__).parent.joinpath("input.txt")


def get_allowed_numbers(rules):
    allowed_numbers = {}
    for rule in rules:
        name, rest = rule.split(": ")
        allowed_numbers[name] = []
        ranges = rest.split(" or ")
        for _range in ranges:
            _from, _to = list(map(int, _range.split("-")))
            allowed_numbers[name] += range(_from, _to + 1)
    return allowed_numbers


def filter_nearby_tickers(allowed_numbers_dict, nearby_tickets):
    allowed_numbers = []
    for allowed in allowed_numbers_dict.values():
        allowed_numbers += allowed
    tickets = []
    for ticket in nearby_tickets:
        values = list(map(int, ticket.split(",")))
        tickets.append(ticket)
        for v in values:
            if v not in allowed_numbers:
                if ticket in tickets:
                    tickets.remove(ticket)
    return tickets


def solve(rules: List[str], nearby_tickets: List[str]) -> int:
    allowed_numbers_dict = get_allowed_numbers(rules)
    allowed_numbers = []
    for allowed in allowed_numbers_dict.values():
        allowed_numbers += allowed
    error_rate = 0

    for ticket in nearby_tickets:
        values = list(map(int, ticket.split(",")))
        for v in values:
            if v not in allowed_numbers:
                error_rate += int(v)

    return error_rate


def solve2(my_ticket, rules: List[str], nearby_tickets: List[str]) -> int:
    allowed_numbers = get_allowed_numbers(rules)
    valid_nearby_tickets = filter_nearby_tickers(allowed_numbers, nearby_tickets)
    rule_pos = {}
    rows = range(len(valid_nearby_tickets[0].split(",")))
    for row in rows:
        rule_pos[row] = []
        for rule in allowed_numbers:
            all_are_valid = True
            for ticket in valid_nearby_tickets:
                value = int(ticket.split(",")[row])
                if value not in allowed_numbers[rule]:
                    all_are_valid = False
                    break
            if all_are_valid:
                rule_pos[row].append(rule)
    result = {}
    while any(rule_pos.values()):
        for row in rule_pos:
            possibilities = rule_pos[row]
            if len(possibilities) == 1:
                result[row] = possibilities[0]
                for rp in rule_pos:
                    if result[row] in rule_pos[rp]:
                        rule_pos[rp].remove(result[row])

    total = 1
    for pos in result:
        if "departure" in result[pos]:
            print(my_ticket[pos])
            total *= int(my_ticket[pos])

    return total


with open(input_file) as input:
    sections: List[str] = input.read().strip().split("\n\n")
    rules = sections[0].split("\n")
    ticket = list(map(int, sections[1].split("\n")[1].split(",")))
    print(ticket)
    nearby_tickets = sections[2].split("\n")[1:]
    print("Solve 1:", solve(rules, nearby_tickets))
    print("Solve 2:", solve2(ticket, rules, nearby_tickets))
