import os
import numpy


def get_data(day):
    return get_example(day), get_input(day)


def get_example(day):
    return open_file(day, "example")


def get_input(day):
    return open_file(day, "input")


def open_file(day, filename):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "..", f"day{day}", f"{filename}.txt")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = numpy.array([line.strip() for line in lines])
    return lines
