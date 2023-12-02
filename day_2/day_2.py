import re


def parse_input(file_name):
    with open(file_name) as f:
        input_txt = f.readlines()
        input_txt = [x.strip() for x in input_txt]
        return input_txt


def solution_day_2_1(input_txt):
    MAX_RED_CUBES = 12
    MAX_GREEN_CUBES = 13
    MAX_BLUE_CUBES = 14
    sum = 0

    # input per line = Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    for line in input_txt:
        # extract the game number
        splitted_line = re.split(":|;", line)
        game = re.search("\d+", splitted_line[0]).group(0)

        INF = False

        max_red_cubes_bag = True  
        max_green_cubes_bag = True
        max_blue_cubes_bag = True
        
        for sub_line in splitted_line[1:]:
            splitted_sub_line = re.split(",", sub_line)
            for sub_sub_line in splitted_sub_line:
                splitted_sub_sub_line = re.split(" ", sub_sub_line)
                if "red" in splitted_sub_sub_line and max_red_cubes_bag:
                    max_red_cubes_bag = True if int(splitted_sub_sub_line[1]) <= MAX_RED_CUBES  else False
                if "green" in splitted_sub_sub_line and max_green_cubes_bag:
                    max_green_cubes_bag = True if int(splitted_sub_sub_line[1]) <= MAX_GREEN_CUBES else False
                if "blue" in splitted_sub_sub_line and max_blue_cubes_bag:
                    max_blue_cubes_bag = True if int(splitted_sub_sub_line[1]) <= MAX_BLUE_CUBES else False  

        if max_red_cubes_bag == False or max_green_cubes_bag == False or max_blue_cubes_bag == False:
            continue
        else:
            sum += int(game)

    return sum


def solution_day_2_2(input_txt):
    sum = 0

    # input per line = Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    for line in input_txt:
        splitted_line = re.split(":|;", line)

        red_cube_values = []
        green_cube_values = []
        blue_cube_values = []

        for sub_line in splitted_line[1:]:  # ignore the game number
            bag = sub_line.split(",")
            for cube in bag:
                cube_color = cube.split(" ")
                if "red" in cube_color:
                    red_cube_values.append(int(cube_color[1]))
                if "green" in cube_color:
                    green_cube_values.append(int(cube_color[1]))
                if "blue" in cube_color:
                    blue_cube_values.append(int(cube_color[1]))

        sum += max(red_cube_values) * max(green_cube_values) * max(blue_cube_values)

    return sum


if __name__  == "__main__":
    print(solution_day_2_1(parse_input("input.txt")))
    print(solution_day_2_2(parse_input("input.txt")))
    