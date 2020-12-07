from pathlib import Path
from typing import List

input_file = Path(__file__).parent.joinpath("input.txt")


def parse(rules: List[str]):
    rulebook = {}
    for rule in rules:
        parts = rule.split(" contain ")
        id = parts[0].replace("bags", "bag").strip()

        if parts[1] == "no other bags.":
            rulebook[id] = {}
        else:
            bags_rules = parts[1][:-1].split(", ")
            supported_rules = {}
            for br in bags_rules:
                amount = int(br[0])
                _id = br[1:].replace("bags", "bag").strip()
                supported_rules[_id] = amount
            rulebook[id] = supported_rules
    return rulebook


def count_bag(bag_id, rulebook):
    # print(bag_id)
    found_bag_ids = []
    for bag in rulebook:
        inner_bag = rulebook[bag]
        if bag_id in inner_bag:
            found_bag_ids.append(bag)
            found_bag_ids = found_bag_ids + count_bag(bag, rulebook)
    return found_bag_ids


def count_bag2(bag_id, rulebook):
    count = 0
    inner_bags = rulebook[bag_id]
    for bag in inner_bags:
        count = count + inner_bags[bag]
        count = count + (inner_bags[bag] * count_bag2(bag, rulebook))
    return count


def solve1(rules: List[str]):
    rulebook = parse(rules)
    count = set(count_bag("shiny gold bag", rulebook))
    return len(count)


def solve2(rules: List[str]):
    rulebook = parse(rules)
    return count_bag2("shiny gold bag", rulebook)


with open(input_file) as input:
    rules = input.read().strip().split("\n")
    print("Solve 1:", solve1(rules))
    print("Solve 1:", solve2(rules))
    # print("Solve 2:", sum(solve2(lines)))
