import re
from math import prod


def parse_input(file_name):
    with open(file_name) as f:
        input_txt = f.readlines()
        input_txt = [x.strip() for x in input_txt]
        return input_txt

# Time = 7ms, Distance = 9mm 
# break the distance in same time of max 7ms: 
# Button Hold time: 0ms ->  0mm travel distance -> 7ms time left * 0mm/ms =  0mm
# Button Hold time: 1ms ->  6mm travel distance -> 6ms time left * 1mm/ms =  6mm
# Button Hold time: 2ms -> 10mm travel distance -> 5ms time left * 2mm/ms = 10mm
# Button Hold time: 3ms -> 12mm travel distance -> 4ms time left * 3mm/ms = 12mm
# Button Hold time: 4ms -> 12mm travel distance -> 3ms time left * 4mm/ms = 12mm
# Button Hold time: 5ms -> 10mm travel distance -> 2ms time left * 5mm/ms = 10mm
# Button Hold time: 6ms ->  6mm travel distance -> 1ms time left * 6mm/ms =  6mm
# Button Hold time: 7ms ->  0mm travel distance -> 0ms time left * 7mm/ms =  0mm
# Which hold time beats the current record of 9mm/7ms? -> 4 different times: 2ms, 3ms, 4ms, 5ms -> 4 is the answer here.
# Which mathematical function can we use? -> f(x) = x * (7 - x) = 7x - x^2 -> f(2) = 12, f(3) = 12, f(4) = 12, f(5) = 10
def solution_day_6_1(input_txt):
    time = input_txt[0]
    distance = input_txt[1]
    solutions = []

    for race in range(len(input_txt[0])):
        counter = 0
        for holding_time in range(1, time[race]):
            dist = calculate_distance(time[race], holding_time)
            counter += 1 if dist > distance[race] else 0
        solutions.append(counter)

    return prod(solutions)


def calculate_distance(race_time, time):
    return time * (race_time - time)


# [[7, 15, 30], [9, 40, 200]]
def prepare_input(input_txt):
    input = []

    for i in range(len(input_txt)):
        input.append(list(map(int, re.findall(r'\d+', input_txt[i]))))

    return input


if __name__  == "__main__":
    print(f"Solution 1: {solution_day_6_1(prepare_input(parse_input('input.txt')))}")
