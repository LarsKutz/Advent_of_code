import re


def parse_input(file_name):
    with open(file_name) as f:
        input_txt = f.readlines()
        input_txt = [x.strip() for x in input_txt]
        return input_txt


# 1 match = 1 point = 2^0
# 2 match = 2 point = 2^1
# 3 match = 4 point = 2^2
# 4 match = 8 point = 2^3
# ...
def solution_day_4_1(input_txt):
    points = []

    for line in input_txt:
        splitted_line = re.split(r':|\|', line)
        winning_numbers = set(splitted_line[1].split())
        my_numbers = set(splitted_line[2].split())

        same_numbers = winning_numbers & my_numbers
        if same_numbers:
            points.append(2**(len(same_numbers)-1))

    return sum(points)


if __name__  == "__main__":
    print(solution_day_4_1(parse_input("input.txt")))
