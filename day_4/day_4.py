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



# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53 -> 4 (2, 3, 4, 5) additional scratchcards
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19 -> 2 (3, 4) additional scratchcards
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1 -> 2 (4, 5) additional scratchcards
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83 -> 1 (5) additional scratchcards
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36 -> 0 additional scratchcards
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11 -> 0 additional scratchcards
# -> 30 additional scratchcards
def solution_day_4_2(input_txt):
    card_amounts = [1] * len(input_txt)

    for line in input_txt:
        splitted_line = re.split(r':|\|', line)
        card_num = int(re.search(r'\d+', splitted_line[0]).group())
        winning_numbers = set(splitted_line[1].split())
        my_numbers = set(splitted_line[2].split())

        same_numbers = winning_numbers & my_numbers

        if same_numbers:       
            for i in range(len(same_numbers)):
                card_amounts[card_num+i] += card_amounts[card_num-1]
    
    return sum(card_amounts)


if __name__  == "__main__":
    print(solution_day_4_1(parse_input("input.txt")))
    print(solution_day_4_2(parse_input("input.txt")))
