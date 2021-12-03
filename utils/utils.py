import os


def get_data(day):
    return get_example(day), get_input(day)


def get_example(day):
    return open_file(day, "example")


def get_input(day):
    return open_file(day, "input")


def open_file(day, filename):
    script_dir = os.path.dirname(__file__)
    file = open(os.path.join(script_dir, "..", f"day{day}", f"{filename}.txt"), 'r')

    lines = file.readlines()
    lines = [line.strip() for line in lines]
    file.close()

    return lines
