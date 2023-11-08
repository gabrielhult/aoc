import string

def read_input():
    with open("3.txt", "r") as f:
        input_data = f.read().split("\n")
        #print(input_data)
    return input_data

def part1(data):
    lower_score = dict(zip(string.ascii_lowercase, range(1,27)))
    higher_score = dict(zip(string.ascii_uppercase, range(27, 53)))
    scores = lower_score | higher_score

    total = 0
    for rucksack in data:
        r_size = len(rucksack)
        first = rucksack[:(len(rucksack) // 2)]
        second = rucksack[(len(rucksack) // 2):]

        first_set = set(first)
        second_set = set(second)

        if(first_set & second_set):
            common = str(first_set & second_set)
            for key in scores:
                if common[2] == key:
                    total += scores.get(common[2])
    return total

def part2(data):
    lower_score = dict(zip(string.ascii_lowercase, range(1,27)))
    higher_score = dict(zip(string.ascii_uppercase, range(27, 53)))
    scores = lower_score | higher_score

    total = 0

    for i in range(0, (len(data)+1) // 3): #Wanted to try zip, maybe a later improvement?
        first = data[3*i]
        second = data[3*i+1]
        third = data[3*i+2]

        first_set = set(first)
        second_set = set(second)
        third_set = set(third)

        if(first_set & second_set & third_set):
                common = str(first_set & second_set & third_set)
                for key in scores:
                    if common[2] == key:
                        total += scores.get(common[2])

    return total






if __name__ == "__main__":
    data = read_input()
    print(part1(data))
    print(part2(data))