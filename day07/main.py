from utils import utils
from math import inf
from numpy import array, percentile


def calc_min_fuel(crabs):
    position = int(percentile(crabs, 50))

    fuel = 0
    for crab in crabs:
        fuel += abs(crab - position)

    return fuel


def calc_min_fuel_with_rate(crabs):
    min_position = min(crabs)
    max_position = max(crabs)

    min_fuel = inf
    for position in range(min_position, max_position + 1):
        fuel = 0

        for crab in crabs:
            diff = abs(position - crab)
            fuel += int(diff * (diff + 1)/2)

        if fuel < min_fuel:
            min_fuel = fuel

    return min_fuel


example_data, input_data = utils.get_data("07")
example_data = array(example_data[0].split(',')).astype(int)
input_data = array(input_data[0].split(',')).astype(int)

example_answer1 = calc_min_fuel(example_data)
input_answer1 = calc_min_fuel(input_data)

example_answer2 = calc_min_fuel_with_rate(example_data)
input_answer2 = calc_min_fuel_with_rate(input_data)

print("## Part 1 ##")
print(f"Answer: {example_answer1}")
print(f"Answer: {input_answer1}\n")

print("## Part 2 ##")
print(f"Answer: {example_answer2}")
print(f"Answer: {input_answer2}\n")
