import os
import math

WINDOW_SIZE = 3

script_dir = os.path.dirname(__file__)
file = open(os.path.join(script_dir, 'input.txt'), 'r')

lines = file.readlines()
lines = [line.strip() for line in lines]

windows = []
counter = 0
previous_value = math.inf

for index in range(0, len(lines) - WINDOW_SIZE + 1):
    value = 0

    for nextIndex in range(0, WINDOW_SIZE):
        value += int(lines[index + nextIndex])

    if value > previous_value:
        counter += 1

    previous_value = value

print(f"There are {counter} sums that are larger than the previous sum")
