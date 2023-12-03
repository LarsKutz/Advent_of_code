
def parse_input(file_name):
    with open(file_name) as f:
        input_txt = f.readlines()
        input_txt = [x.strip() for x in input_txt]
        return input_txt


# Idea1: Combine numbers and add aditional numbers to list with his length
#        Example: 4  6  7  .  .  1  1  4  .  .  -> 467 467 467 . . 114 114 114 . . 
#                 .  .  .  *  .  .  .  .  .  .  ->  .   .   .  * .  .   .   .  . .  
# Idea2: Look for each digit if there is a symbol around it. After that add numbers
#        that are adjacent this the digit.
# Idea3: Add padding (add "." around the input) like in convolutional neural networks. This way we can check easily the 
#        environment of each digit without errors at the edges.    <------ This one is the best one
def solution_day_3_1(input_txt):
    numbers = []    # List of numbers with symbol(s) around them  

    checks = [(-1,-1),  # Top left
            (-1,0),     # Top middle
            (-1,1),     # Top right
            (0,-1),     # Mid left
            (0,1),      # Mid right
            (1,-1),     # Bottom left
            (1,0),      # Bottom middle
            (1,1)]      # Bottom right

    # symbols are everything except and points
    for line in range(1, len(input_txt) - 1):
        current_num = ""
        num_has_symbol = False

        for char in range(1, len(input_txt[0]) - 1):
            
            if input_txt[line][char].isdigit():
                current_num += input_txt[line][char]
                # print(input_txt[line][char])  

                # Check environment with distance of 1 in all directions
                for check in checks:
                    if input_txt[line+check[0]][char+check[1]] == ".":
                        # print(f"Point found at {check}")
                        pass
                    elif input_txt[line+check[0]][char+check[1]].isdigit():
                        # print(f"Digit found at {check}")
                        pass
                    else:
                        # print(f"Symbol found at {check}")
                        num_has_symbol = True

                # To add numbers that are at the end of the line
                if char == len(input_txt[0]) - 2:
                    if current_num != "" and num_has_symbol == True:
                        numbers.append(int(current_num))
                        current_num = ""
                        num_has_symbol = False
                    else:
                        current_num = ""
                        num_has_symbol = False
            else:
                if current_num != "" and num_has_symbol == True:
                    numbers.append(int(current_num))
                    current_num = ""
                    num_has_symbol = False
                else:
                    current_num = ""
                    num_has_symbol = False

    return sum(numbers)



def solution_day_3_2(input_txt):
    numbers = []    

    checks = [(-1,-1),  # Top left
            (-1,0),     # Top middle
            (-1,1),     # Top right
            (0,-1),     # Mid left
            (0,1),      # Mid right
            (1,-1),     # Bottom left
            (1,0),      # Bottom middle
            (1,1)]      # Bottom right
    
    for line in range(1, len(input_txt) - 1):
        for char in range(1, len(input_txt[0]) - 1):
            if input_txt[line][char] == "*":
                numbers_set = set()
                for check in checks:
                    if input_txt[line+check[0]][char+check[1]].isdigit():
                        number = input_txt[line+check[0]][char+check[1]]

                        counter = 1
                        # run left 
                        while input_txt[line+check[0]][char+check[1]-counter].isdigit():
                            number = input_txt[line+check[0]][char+check[1]-counter] + number
                            counter += 1  

                        counter = 1
                        # run right
                        while input_txt[line+check[0]][char+check[1]+counter].isdigit():
                            number = number + input_txt[line+check[0]][char+check[1]+counter]
                            counter += 1
                        numbers_set.add(number)   

                if len(numbers_set) == 2:
                    numbers.append(int(numbers_set.pop()) * int(numbers_set.pop()))

    return sum(numbers)            


def prepare_input(input_txt):
    input_with_padding = []
    width = len(input_txt[0])

    input_with_padding.append("."*(width+2))
    for line in input_txt:
        input_with_padding.append("." + line + ".")
    input_with_padding.append("."*(width+2))

    return input_with_padding


if __name__  == "__main__":
    print(solution_day_3_1(prepare_input(parse_input("input.txt"))))
    print(solution_day_3_2(prepare_input(parse_input("input.txt"))))
