import math
from utils import utils


def calc_number_of_increase(data):
    previous_value = math.inf
    counter = 0

    for line in data:
        if (value := int(line)) > previous_value:
            counter += 1

        previous_value = value

    return counter


def calc_number_of_increase_with_window(data, window_size):
    previous_value = math.inf
    counter = 0

    for index in range(0, len(data) - window_size + 1):
        value = 0

        for nextIndex in range(0, window_size):
            value += int(data[index + nextIndex])

        if value > previous_value:
            counter += 1

        previous_value = value

    return counter


example_data, input_data = utils.get_data("01")

example_count = calc_number_of_increase(example_data)
input_count = calc_number_of_increase(input_data)

print("## Part 1 ##")
print(f"Result for example: {example_count}")
print(f"Result for input: {input_count}")

WINDOW_SIZE = 3
example_count = calc_number_of_increase_with_window(example_data, WINDOW_SIZE)
input_count = calc_number_of_increase_with_window(input_data, WINDOW_SIZE)

print("## Part 2 ##")
print(f"Result for example: {example_count}")
print(f"Result for input: {input_count}")
