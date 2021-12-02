import math
import os

script_dir = os.path.dirname(__file__)
file = open(os.path.join(script_dir, 'input.txt'), 'r')

lines = file.readlines()
lines = [line.strip() for line in lines]
file.close()

previous_value = math.inf
counter = 0

for line in lines:
    if (value := int(line)) > previous_value:
        counter += 1

    previous_value = value

print(f"There are {counter} measurements that are larger than the previous measurement")
