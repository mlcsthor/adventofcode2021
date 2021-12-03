from utils import utils


def calc_pos_and_depth(data):
    position = 0
    depth = 0

    for line in data:
        direction, value = line

        if direction == "forward":
            position += int(value)
        else:
            depth += int(value) * (-1 if direction == "up" else 1)

    return position, depth


def calc_pos_and_depth_with_aim(data):
    position = 0
    depth = 0
    aim = 0

    for line in data:
        direction, value = line

        if direction == "forward":
            position += int(value)
            depth += aim * int(value)
        else:
            aim += int(value) * (-1 if direction == "up" else 1)

    return position, depth


def print_answer(label, position, depth):
    print(f"Result for {label} data:")
    print(f"Position: {position}, Depth: {depth}")
    print(f"Answer: {position * depth}\n")


example_data, input_data = utils.get_data("02")

example_data = [line.split() for line in example_data]
input_data = [line.split() for line in input_data]

example_pos, example_depth = calc_pos_and_depth(example_data)
input_pos, input_depth = calc_pos_and_depth(input_data)

print("## Part 1 ##")
print_answer("example", example_pos, example_depth)
print_answer("input", input_pos, input_depth)

example_pos, example_depth = calc_pos_and_depth_with_aim(example_data)
input_pos, input_depth = calc_pos_and_depth_with_aim(input_data)

print("## Part 2 ##")
print_answer("example", example_pos, example_depth)
print_answer("input", input_pos, input_depth)
