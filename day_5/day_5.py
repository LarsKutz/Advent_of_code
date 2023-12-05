import re
from collections import defaultdict
from time import time


def parse_input(file_name):
    with open(file_name) as f:
        input_txt = f.read()
        input_txt = input_txt.split("\n\n")
        input_txt = [x.replace("\n", ";") for x in input_txt]
        return input_txt


def converter(rules, val):
    for rule in rules:
        if val < rule[1] or val > rule[1] + rule[2] - 1:
            continue
        else:
            dest = rule[0]
            src = rule[1]

            return dest + val - src

    return val


"""
{
    "seeds": [79, 14, 55, 13],
    "seed-to-soil": [[50, 98, 2], [52, 50, 48]],   # [[dest, source, range], [dest, source, range]]
    "soil-to-fertilizer": [[0, 15, 37], [37, 52, 2], [39, 0, 15]],
    "ferilizer-to-water": [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]],
    "water-to-light": [[88, 18, 7], [18, 25, 70]],
    "light-to-temperature": [[45, 77, 23], [81, 45, 19], [68, 64, 13]],
    "temperature-to-humidity": [[0, 69, 1], [1, 0, 69]],
    "humidity-to-location": [[60, 56, 37], [56, 93, 4]],
}
solution: [82, 43, 86, 35]
"""
def solution_day_5_1(input_dic):
    seeds = input_dic["seeds"]
    locations = [1] * len(seeds)
    
    for i, seed in enumerate(seeds):
        current_seed = seed
        for values in list(input_dic.values())[1:]:
            current_seed = converter(values, current_seed)
            locations[i] = current_seed

    return min(locations)


def get_seeds(seeds):
    # create paris from seeds list. First value ist start, secon is range
    # [79, 14, 55, 13] -> 79 + 14 = 79...92 seeds, 55 + 13 = 55...67 seeds
    # seeds = [[79, 14], [55, 13]
    # return [79, 80, ..., 92, 55, 56, ..., 67]
    seed_pairs = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]

    return [x for pair in seed_pairs for x in range(pair[0], pair[0] + pair[1])]

def solution_day_5_2(input_dic):
    seeds = get_seeds(input_dic["seeds"])
    locations = [1] * len(seeds)

    for i, seed in enumerate(seeds):
        current_seed = seed
        for values in list(input_dic.values())[1:]:
            current_seed = converter(values, current_seed)
            locations[i] = current_seed

    return min(locations)


def prepare_data(input_txt):
    dic = defaultdict(list)
    seed_values = re.findall(r"\d+", input_txt[0])
    seed_values = [int(x) for x in seed_values]
    dic[re.findall(r"\w+", input_txt[0])[0]] = seed_values
    
    for i in input_txt[1:]:
        key = re.findall(r"\w+-to-\w+", i)[0]
        values = re.split(r";", i)
        for value in values[1:]:
            dic[key].append(re.findall(r"\d+", value))

    # convert to int
    for v in list(dic.values())[1:]:
        for i in range(len(v)):
            for j in range(len(v[i])):
                v[i][j] = int(v[i][j])
    
    return dic


if __name__  == "__main__":
    start_time = time()
    #print(f"Solution 1: {solution_day_5_1(prepare_data(parse_input('input.txt')))}, time: {time() - start_time}")
    start_time = time()
    print(f"Solution 2: {solution_day_5_2(prepare_data(parse_input('input.txt')))}, time: {time() - start_time}")
