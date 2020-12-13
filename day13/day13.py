from pathlib import Path
from typing import List

input_file = Path(__file__).parent.joinpath("input.txt")


def solve(time: int, bus_ids: List[int]) -> int:
    for current_time in range(time, time + 10):
        for id in bus_ids:
            if current_time % id == 0:
                return id * (current_time - time)
    return 0


def solve2_naive(
    time: int,
    bus_ids: List[int],
    ids_and_x: List[str],
) -> int:
    while time:
        bus_leaving_counter: int = 0
        for id in bus_ids:
            depart_at: int = time + ids_and_x.index(str(id))
            if not depart_at % id == 0:
                break
            bus_leaving_counter += 1
        if bus_leaving_counter == len(bus_ids):
            return time
        time += 1
    return 0


# To understand and write the chinese_remainder_theorem I've used theses:
# https://brilliant.org/wiki/chinese-remainder-theorem/#see-also
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem
# https://math.stackexchange.com/questions/79282/solving-simultaneous-congruences
# https://docs.python.org/3/library/functions.html?highlight=pow#pow
# Big thanks to the following for helping me bridge the theory with the code
# https://fangya.medium.com/chinese-remainder-theorem-with-python-a483de81fbb8
# https://github.com/elvinyhlee/advent-of-code-2020-python/blob/master/day13.py
# u/thomasahle
def chinese_remainder_theorem(
    pairwise_coprime_n: List[int], arbitrary_a: List[int]
) -> int:
    product = 1
    # Step 1 compute N
    for ni in pairwise_coprime_n:
        product *= ni
    sum = 0
    for ni, ai in zip(pairwise_coprime_n, arbitrary_a):
        yi = product // ni  # step 2 find the yi
        zi = pow(yi, -1, mod=ni)  # Step 3 compute zi
        sum += ai * zi * yi  # Step 4 compute the sum
    return sum % product  # The modulo of sum product is the smallest time


def solve2(
    time: int,
    bus_ids: List[int],
    ids_and_x: List[str],
) -> int:
    arbitrary_a_simultaneous_congruences = [
        bid - ids_and_x.index(str(bid)) for bid in bus_ids
    ]
    return chinese_remainder_theorem(bus_ids, arbitrary_a_simultaneous_congruences)


with open(input_file) as input:
    time, bus_ids = input.read().strip().split("\n")
    ids = list(map(int, bus_ids.replace(",x", "").split(",")))
    ids_and_x = bus_ids.split(",")
    print("Solve 1:", solve(int(time), ids))
    # print("Solve 2 naive:", solve2_naive(int(time), ids, ids_and_x))
    print("Solve 2:", solve2(int(time), ids, ids_and_x))