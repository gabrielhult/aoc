import ast

right_order_ctr = 0
right_order = 0

def read_input():
    with open("13.txt", "r") as f:
        input_data = f.read().split("\n")        
    return input_data


def traverse_lst(left, right):
    global right_order
    global right_order_ctr
    if(len(left) > 0 and len(right) > 0):
        if(isinstance(left[0], int) and isinstance(right[0], list) or isinstance(left[0], list) and isinstance(right[0], int)):
            if(isinstance(left[0], list) and isinstance(right[0], int)):
                return traverse_lst(left[0], [right[0]])
            else:
                return traverse_lst([left[0]], right[0])
        elif(isinstance(left[0], int) and isinstance(right[0], int)): #both are integers
            if left[0] < right[0]:
                return right_order_ctr
            elif left[0] == right[0]:
                return traverse_lst(left[1:], right[1:])
            else:
                return -1
        elif(isinstance(left[0], list) and isinstance(right[0], list)): #both are lists
            if(traverse_lst(left[0], right[0]) > 0):
                return right_order_ctr
            elif(traverse_lst(left[0], right[0]) < 0):
                return -1
            else:
                return traverse_lst(left[1:], right[1:])
    elif(len(left) == 0 and len(right) > 0):
        return right_order_ctr
    elif(len(left) > 0 and len(right) == 0):
        return -1
    else:
        return 0



def part1(data):
    pairs = []
    current_pair = []
    right_order = 0
    global right_order_ctr

    #Preparing the input data
    for item in data:
        if(item != ''):
            item = ast.literal_eval(item) #this is trusted data :)
            current_pair.append(item)
        else:
            pairs.append(current_pair)
            current_pair = []
    pairs.append(current_pair)

    #Performing the algorithm
    for pair in pairs:
        right_order_ctr += 1
        left = pair[0]
        right = pair[1]
        res = traverse_lst(left, right)
        if(res > 0):
            right_order += res
    return right_order

def part2(data):
    pairs = []
    current_pair = []
    #Preparing the input data
    for item in data:
        if(item != ''):
            item = ast.literal_eval(item) #this is trusted data :)
            pairs.append(item)

    pairs.append([[2]])
    pairs.append([[6]])

    right_order = 0
    global right_order_ctr
    #Performing the algorithm
    while(True):
        right_order_ctr = 0
        changed = False
        for idx in range(len(pairs)-1):

            right_order_ctr += 1
            left = pairs[idx]
            right = pairs[idx+1]
            res = traverse_lst(left, right)
            if(res < 0):
                pairs[idx+1] = pairs[idx]
                pairs[idx] = right
                changed = True
        if(not changed):
            break
    for elem in range(len(pairs)):
        if(pairs[elem] == [[2]]):
            first = elem+1
        elif(pairs[elem] == [[6]]):
            second = elem+1
    return first * second


if __name__ == "__main__":
    data = read_input()
    print(part1(data))
    print(part2(data))