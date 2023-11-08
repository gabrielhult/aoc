def read_input():
    with open("aoc_22/1.txt", "r") as f:
        input_data = f.read().split("\n")
    return input_data

def part1(calories_list):
    highest = 0
    current = 0

    for item in calories_list:
        if item == '':
            if(current > highest):
                highest = current
            current = 0
        else:
            current += int(item) 
    return highest

def part2(calories_list):
    highest = []
    current = 0

    for item in calories_list:
        if item == '':
            if(len(highest) < 3):
                highest.append(current)
            else:
                lowest_highest = highest.index(min(highest))
                if(current > highest[lowest_highest]):
                    highest[lowest_highest] = current
            current = 0
        else:
            current += int(item)
    return sum(highest, 0)




if __name__ == "__main__":
    calories_list = read_input()
    print(part1(calories_list))
    print(part2(calories_list))