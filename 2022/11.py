def read_input():
    with open("11.txt", "r") as f:
        input_data = f.read().split("\n")
    return input_data

def format_monkey_data(data):
    formatted_data = []
    start = 0
    end = start + 6
    formatted_loop = data[0::7]
    worry_level = 0

    for monkey in formatted_loop:
        monkey_formatted = []
        #Monkey index
        monkey_properties = []
        monkey_formatted.append(monkey[7])

        #Monkey items
        monkey_inventory = []
        monkey_items = data[start+1].split(":")[1].split(",")
        for item in monkey_items:
            if item[1:2].isdigit():
                monkey_inventory.append(int(item))
        monkey_formatted.append(monkey_inventory)

        #Monkey Operation
        operation = []
        monkey_operation = data[start+2].split(":")[1]
        operation.append(monkey_operation[11])
        if(monkey_operation[13:].isdigit()):
            operation.append(int(monkey_operation[13:]))
        else:
            operation.append(monkey_operation[13:])
        monkey_formatted.append(operation)

        #Monkey divisible test
        monkey_formatted.append(int(data[start+3][-2:]))

        #Monkey if true or false
        monkey_formatted.append(int(data[start+4][-1]))
        monkey_formatted.append(int(data[start+5][-1]))

        #Monkey inspection counter
        monkey_formatted.append(0)

        formatted_data.append(monkey_formatted) #ändra till monkey_formatted
        start += 7
        end = start + 7
    return formatted_data

def part1(data):
    formatted_data = format_monkey_data(data)
    for _ in range(20):
        for monkey in formatted_data:
            while(len(monkey[1]) != 0):
                worry_level = monkey[1].pop(0)
                if(monkey[2][0][0] == '*'):
                    if(type(monkey[2][1]) == int):
                        worry_level *= monkey[2][1]
                    else:
                        worry_level *= worry_level
                else:
                    if(type(monkey[2][1]) == int):
                        worry_level += monkey[2][1]
                    else:
                        worry_level += worry_level
                
                worry_level = worry_level // 3
                if(worry_level % monkey[3] == 0):
                    formatted_data[monkey[4]][1].append(worry_level)
                else:
                    formatted_data[monkey[5]][1].append(worry_level)
                monkey[6] += 1


    inspections = [monkey[6] for monkey in formatted_data]
    business_one = max(inspections)
    inspections.remove(max(inspections))
    business_two = max(inspections)
    return business_one * business_two

def part2(data):
    formatted_data = format_monkey_data(data)
    supermodulo = 1
    for monkey in formatted_data:
        for item in monkey[1]:
            supermodulo = supermodulo * item

    for _ in range(10000):
        for monkey in formatted_data:
            while(len(monkey[1]) != 0):
                worry_level = monkey[1].pop(0) % supermodulo
                if(monkey[2][0][0] == '*'):
                    if(type(monkey[2][1]) == int):
                        worry_level *= monkey[2][1]
                    else:
                        worry_level *= worry_level
                else:
                    if(type(monkey[2][1]) == int):
                        worry_level += monkey[2][1]
                    else:
                        worry_level += worry_level
                
                if(worry_level % monkey[3] == 0):
                    formatted_data[monkey[4]][1].append(worry_level)
                else:
                    formatted_data[monkey[5]][1].append(worry_level)
                monkey[6] += 1

    inspections = [monkey[6] for monkey in formatted_data]
    business_one = max(inspections)
    inspections.remove(max(inspections))
    business_two = max(inspections)
    return business_one * business_two


if __name__ == "__main__":
    data = read_input()
    print(part1(data))
    print(part2(data))