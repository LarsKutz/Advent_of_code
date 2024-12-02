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


def solution_day_1_2(input_txt):
    sum = 0

    # Idea: replace nnumbers with double initial and final letters
    # that i can handle numbers that are connected like e.g. "eightwo" -> eeighttttwoo
    # After thati can replace every word with his number without any problems
    # and remove all non digits, so i have a clean string with only digits
    # and can get the first and last digit and add them together
    # Example 1: "two1nine"         -> ttwoo1nninee             ->   219
    # Example 2: "eightwothree"     -> eeighttttwootthreee      ->   823
    # Example 3: "abcone2threexyz"  -> abcoonee2tthreeexyz      ->   123
    # Example 4: "4nineeightseven2" -> 4nnineeeeighttssevenn2   -> 49872
    # Example 5: "zoneight234"      -> zooneeeeightt234         -> 18234
    # Example 6: "7pqrstsixteen"    -> 7pqrstssixxteen          ->    76

    replace_num_with_words = {
        "zero": "zzeroo",   
        "one": "oonee",     
        "two": "ttwoo",     
        "three": "tthreee",
        "four": "ffourr",
        "five": "ffivee",
        "six": "ssixx",
        "seven": "ssevenn",
        "eight": "eeightt",
        "nine": "nninee"}
    
    replace_words_with_num = {
        "zero": "0",   
        "one": "1",     
        "two": "2",     
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"}

    for line in input_txt:
        first_digit = None
        last_digit = None

        # replace numbers with words
        for k,v in replace_num_with_words.items():
            line = line.replace(k, v)

        # replace words with numbers
        for k,v in replace_words_with_num.items():
            line = line.replace(k, v)

        # removce all non digits
        line = re.sub(r"[a-zA-Z]+", "", line)
        first_digit = line[0]
        last_digit = line[-1]

        sum += int(first_digit + last_digit)

    return sum


if __name__  == "__main__":
    print(solution_day_1_1(parse_input("input.txt")))
    print(solution_day_1_1_v2(parse_input("input.txt")))
    print(solution_day_1_2(parse_input("input.txt")))
    