from utils import utils
import numpy


def calc_number_of_fish(data, days):
    for d in range(days):
        print(f"Day {d + 1}")
        new = [8 for _ in numpy.where(data - 1 == -1)[0]]

        for i in range(len(data)):
            d = data[i] - 1
            data[i] = d if d != -1 else 6

        data = numpy.append(data, new).astype(int)

    return len(data)


example_data, input_data = utils.get_data("06")
example_data = numpy.array(example_data[0].split(',')).astype(int)
input_data = numpy.array(input_data[0].split(',')).astype(int)

example_answer1 = calc_number_of_fish(example_data, 80)
input_answer1 = calc_number_of_fish(input_data, 80)

print("## Part 1 ##")
print(f"Answer: {example_answer1}")
print(f"Answer: {input_answer1}\n")
