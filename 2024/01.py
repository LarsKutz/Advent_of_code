import re


def load_file(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        return lines


def solve_1(file_input):
    left = []
    right = []
    for input in file_input:
        t = re.findall(r"\d+", input)
        left.append(int(t[0]))
        right.append(int(t[1]))
    
    left.sort()
    right.sort()
    
    d = 0
    for l, r in zip(left, right):
        d += abs(l-r)
    
    return d


def solve_2(file_input):
    left = []
    right = []
    for input in file_input:
        t = re.findall(r"\d+", input)
        left.append(int(t[0]))
        right.append(int(t[1]))
    
    d = 0
    for l in left:
        m = right.count(l)
        d += l*m
    
    return d


if __name__ == '__main__':
    file_exa = "Examples/01_2.txt"
    file_inp = "Inputs/01_2.txt"
    file_input = load_file(file_inp)
    # print(solve_1(file_input))
    print(solve_2(file_input))
