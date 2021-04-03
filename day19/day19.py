from ast import parse
from pathlib import Path
from typing import Dict, List, Optional
from itertools import product, permutations, combinations, chain
from collections import OrderedDict 
import operator

input_file: Path = Path(__file__).parent.joinpath("input.txt")

def solve(rules: List[str], messages:List[str]) -> int:
    total = 0
    parsed_rules: Dict[str, str] = {}
    rule_id_constraints  = {}
    for rule in rules:
        _id, constraints = rule.split(": ")
        rule_id_constraints[_id] = constraints
    
    ordered_rules = {}
    for i in range(len(rules)):
        ordered_rules[i] = rule_id_constraints[f"{i}"]
    ordered_rules = list(reversed(ordered_rules.items()))
    
    # Parse "Root rules"
    for _id, constraints in ordered_rules:
        if '"' in constraints:
            constraints = constraints.replace("\"","")
            parsed_rules[_id] = []
            parsed_rules[_id].append(constraints)

    while len(parsed_rules) != len(rules):
        for _id, constraints in ordered_rules:
            
            for constraint in constraints.split("|"):
                if '"' not in constraint:
                    if all([int(_rule) in parsed_rules for _rule in constraint.split()]):
                        if _id not in parsed_rules:
                            parsed_rules[_id] = []
                        _rules = [parsed_rules[int(_rule)] for _rule in constraint.split()]
                        #print(_rules)
                        for rule_combination in permutations(chain.from_iterable(_rules)):
                            parsed_rules[_id].append("".join(rule_combination))
    for message in messages:
        complete_match = [part == message for part in parsed_rules[0]]
        
        #print(message, any(complete_match))
        if any(complete_match):
            total += 1

    return total


with open(input_file) as input:
    rules, messages = input.read().strip().split("\n\n")
    rules = rules.split("\n")
    messages = messages.split("\n")
    
    print("Solve 1:", solve(rules, messages))
    #print("Solve 2:", solve(rows))
