import numpy
from utils import utils


def format_bound(line):
    return [bound.split(',') for bound in line.split('->')]


def extract_bounds(data):
    return numpy.array([format_bound(line) for line in data], dtype=int)


def complete_diagram(size, coordinates, with_diagonal):
    diag = numpy.full([size, size], 0, dtype=int)

    for line in coordinates:
        [x1, y1], [x2, y2] = line
        min_x, max_x = min(x1, x2), max(x1, x2) + 1
        min_y, max_y = min(y1, y2), max(y1, y2) + 1

        if x1 != x2 and y1 != y2:
            if not with_diagonal:
                continue

            x_list = list(range(min_x, max_x))
            if x1 > x2:
                x_list.reverse()

            y_list = list(range(min_y, max_y))
            if y1 > y2:
                y_list.reverse()

            coords = list(zip(x_list, y_list))

            for coord in coords:
                diag[coord[1]][coord[0]] += 1
        else:
            for i in range(min_x, max_x):
                for j in range(min_y, max_y):
                    diag[j][i] += 1

    return diag


def count_overlapping(diagram):
    return numpy.count_nonzero(diagram > 1)


def get_answer(size, data, with_diagonal=False):
    bounds = extract_bounds(data)
    diagram = complete_diagram(size, bounds, with_diagonal)
    return count_overlapping(diagram)


example_data, input_data = utils.get_data("05")

example_answer1 = get_answer(10, example_data)
input_answer1 = get_answer(1000, input_data)

example_answer2 = get_answer(10, example_data, with_diagonal=True)
input_answer2 = get_answer(1000, input_data, with_diagonal=True)

print("## Part 1 ##")
print(f"Answer: {example_answer1}")
print(f"Answer: {input_answer1}\n")

print("## Part 2 ##")
print(f"Answer: {example_answer2}")
print(f"Answer: {input_answer2}\n")