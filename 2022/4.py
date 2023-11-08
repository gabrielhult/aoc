import re

def read_input():
    with open("4.txt", "r") as f:
        input_data = f.read().split("\n")
    return input_data

def part1(data): 
    overlaps = 0
    for pairs in data:
        value = re.split('-|,', pairs)

        if(int(value[0]) <= int(value[2]) and int(value[1]) >= int(value[3])):
            overlaps += 1
        
        elif(int(value[2]) <= int(value[0]) and int(value[3]) >= int(value[1])):
            overlaps += 1
        
    return overlaps

def part2(data):
    overlap = 0
    for pairs in data:
        assigned = re.split('-|,', pairs)
        first_pair_set = set(range(int(assigned[0]), int(assigned[1])+1))
        second_pair_set = set(range(int(assigned[2]), int(assigned[3])+1))
        if(first_pair_set & second_pair_set):
            overlap += 1
    return overlap






if __name__ == "__main__":
    data = read_input()
    print(part1(data))
    print(part2(data))