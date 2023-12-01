import re


def parse_input(file_name):
    with open(file_name) as f:
        input_txt = f.readlines()
        input_txt = [x.strip() for x in input_txt]
        return input_txt


def solution_day_1_1(input_txt):
    sum = 0
    for line in input_txt:
        first_digit = 0
        last_digit = 0
        for word in line:
            if word.isdigit():
                first_digit = word
                break
        for word in reversed(line):
            if word.isdigit():
                last_digit = word
                break
        digit = int(first_digit + last_digit)
        sum += digit
    return sum


def solution_day_1_1_v2(input_txt):
    sum = 0
    for line in input_txt:
        line = re.sub(r"[a-zA-Z]+", "", line)
        digit_1 = line[0]
        digit_2 = line[-1]
        digit = int(digit_1 + digit_2)
        sum += digit 
    return sum


if __name__  == "__main__":
    print(solution_day_1_1(parse_input("input.txt")))
    print(solution_day_1_1_v2(parse_input("input.txt")))
    