import numpy
from utils import utils


def format_bound(line):
    return [bound.split(',') for bound in line.split('->')]


def extract_bounds(data):
    return numpy.array([format_bound(line) for line in data], dtype=int)


def complete_diagram_without_diagonal(size, coordinates):
    diag = numpy.full([size, size], 0, dtype=int)

    for line in coordinates:
        x1, y1 = line[0]
        x2, y2 = line[1]

        if x1 != x2 and y1 != y2:
            continue

        start_x = min(x1, x2)
        end_x = max(x1, x2)

        start_y = min(y1, y2)
        end_y = max(y1, y2)

        for i in range(start_x, end_x + 1):
            for j in range(start_y, end_y + 1):
                diag[j][i] += 1

    return diag


def complete_diagram(size, coordinates):
    diag = numpy.full([size, size], 0, dtype=int)

    for line in coordinates:
        x1, y1 = line[0]
        x2, y2 = line[1]
        diff_x = abs(x1 - x2)
        diff_y = abs(y1 - y2)

        if x1 != x2 and y1 != y2:
            x_list = list(range(min(x1, x2), max(x1, x2) + 1))
            if x1 > x2:
                x_list.reverse()

            y_list = list(range(min(y1, y2), max(y1, y2) + 1))
            if y1 > y2:
                y_list.reverse()

            coords = list(zip(x_list, y_list))

            for coord in coords:
                diag[coord[1]][coord[0]] += 1
        else:
            start_x = min(x1, x2)
            end_x = max(x1, x2)

            start_y = min(y1, y2)
            end_y = max(y1, y2)

            for i in range(start_x, end_x + 1):
                for j in range(start_y, end_y + 1):
                    diag[j][i] += 1

    return diag


def count_overlapping(diagram):
    return numpy.count_nonzero(diagram > 1)


def get_answer_part1(size, data):
    bounds = extract_bounds(data)
    diagram = complete_diagram_without_diagonal(size, bounds)
    return count_overlapping(diagram)


def get_answer_part2(size, data):
    bounds = extract_bounds(data)
    diagram = complete_diagram(size, bounds)
    return count_overlapping(diagram)


example_data, input_data = utils.get_data("05")

example_answer1 = get_answer_part1(10, example_data)
input_answer1 = get_answer_part1(1000, input_data)

example_answer2 = get_answer_part2(10, example_data)
input_answer2 = get_answer_part2(1000, input_data)

print("## Part 1 ##")
print(f"Answer: {example_answer1}")
print(f"Answer: {input_answer1}\n")

print("## Part 2 ##")
print(f"Answer: {example_answer2}")
print(f"Answer: {input_answer2}\n")