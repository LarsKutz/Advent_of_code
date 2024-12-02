from collections import defaultdict, Counter


def parse_input(file_name):
    with open(file_name) as f:
        input_txt = f.readlines()
        input_txt = [x.strip() for x in input_txt]
        return input_txt


# A > K > Q > J > T > 9 > 8 > 7 > 6 > 5 > 4 > 3 > 2
# Five of a kind > 4 of a kind > Full House > 3 of a kind > 2 pair > 1 pair > high card
# Strongness: 5 of a kind: 5, 4 of a kind: 4, Full House: 3, 3 of a kind: 2, 2 pair: 1, 1 pair: 0, high card: -1
# Idea: Figure out which type of strongness each hand has and label them and order them. If the strongness is the same, 
#       compare the beginning card, if the beginning card is the same, compare the next card
# Lowest hand is getting multiplier 1 
def solution_day_7_1(input_txt):
    sum = 0
    next_multiplier = 1
    label_dict = defaultdict(list)

    # Sort the hands by their strongness in a dict
    for hand in input_txt:
        hand_mul = hand.split(" ")
        strongness = check_strongness(hand_mul[0])
        label_dict[strongness].append(hand_mul)

    # Sort the hand by their rank in each strongness
    for values in dict(sorted(label_dict.items())).values():
        sum_hands, next_multiplier = compare_hands(values, next_multiplier)
        sum += sum_hands
    
    return sum


def compare_hands(hands, start_multiplier):
    # A > K > Q > J > T > 9 > 8 > 7 > 6 > 5 > 4 > 3 > 2
    sum = 0
    next_multiplier = start_multiplier

    # sort values by their first character, if the first character is the same, sort by the second character, and so on
    hands = sorted(hands, key=lambda x: x[0])

    for hand in hands:
        sum += int(hand[1]) * next_multiplier
        next_multiplier += 1

    return sum, next_multiplier


def check_strongness(hand):  # input will be e.g. 32T3K 
    hand = Counter(hand)
    if hand.most_common()[0][1] == 5:                           
        return 5    # 5 of a kind
    elif hand.most_common()[0][1] == 4:                                     
        return 4    # 4 of a kind
    elif hand.most_common()[0][1] == 3 and hand.most_common()[1][1] == 2:   
        return 3    # Full House
    elif hand.most_common()[0][1] == 3: # Dont need to check for 2nd most common, because otherwise it would be a full house
        return 2    # 3 of a kind
    elif hand.most_common()[0][1] == 2 and hand.most_common()[1][1] == 2:
        return 1    # 2 pair
    elif hand.most_common()[0][1] == 2:
        return 0    # 1 pair
    else:
        return -1   # high card
        

def prepare_input(input_txt):
    # replace A with Z, because A is the highest card
    # replace K with Y, because K is the second highest card
    # replace Q with X, because Q is the third highest card
    # replace J with W, because J is the fourth highest card
    # replace T with V, because T is the fifth highest card

    modified_texts = []
    for text in input_txt:
        modified_text = text.replace("A", "Z")
        modified_text = modified_text.replace("K", "Y")
        modified_text = modified_text.replace("Q", "X")
        modified_text = modified_text.replace("J", "W")
        modified_text = modified_text.replace("T", "V")
        modified_texts.append(modified_text)

    return modified_texts


if __name__  == "__main__":
    print(f"Solution 1: {solution_day_7_1(prepare_input(parse_input('input.txt')))}")
