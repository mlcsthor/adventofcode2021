from utils import utils
import numpy


def get_most_common_bit(column):
    unique, counts = numpy.unique(column, return_counts=True)
    count = dict(zip(unique, counts))

    return 1 if count['0'] == count['1'] else max(count, key=count.get)


def calc_gamma_and_epsilon_rate(data):
    data_bin = numpy.array([list(line) for line in data])
    gamma_rate = numpy.array([get_most_common_bit(column) for column in data_bin.T])
    epsilon_rate = numpy.invert(gamma_rate.astype(bool)).astype(int)

    return int(''.join(map(str, gamma_rate)), 2), int(''.join(map(str, epsilon_rate)), 2)


def calc_oxygen_and_co2_rate(data):
    oxygen_data = co2_data = data
    
    for i in range(0, len(data[0])):
        oxygen_data = keep_correct_lines(oxygen_data, i)
        co2_data = keep_correct_lines(co2_data, i, is_co2=True)

    return int(oxygen_data[0], 2), int(co2_data[0], 2)


def keep_correct_lines(data, index, is_co2=False):
    if len(data) == 1:
        return data

    binary = numpy.array([list(line) for line in data])
    maximum = int(get_most_common_bit(binary[:, index]))

    if is_co2:
        maximum = 1 - maximum

    data = [line for line in data if line[index] == str(maximum)]

    return data


example_data, input_data = utils.get_data("03")

example_gamma, example_epsilon = calc_gamma_and_epsilon_rate(example_data)
input_gamma, input_epsilon = calc_gamma_and_epsilon_rate(input_data)

print("## Part 1 ##")
print(f"Answer: {example_gamma * example_epsilon}")
print(f"Answer: {input_gamma * input_epsilon}\n")

example_oxygen, example_co2 = calc_oxygen_and_co2_rate(example_data)
input_oxygen, input_co2 = calc_oxygen_and_co2_rate(input_data)

print("## Part 2 ##")
print(f"Answer: {example_oxygen * example_co2}")
print(f"Answer: {input_oxygen * input_co2}")
