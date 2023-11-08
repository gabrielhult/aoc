def read_input():
    with open("5.txt", "r") as f:
        input_data = f.read().split("\n")
        columns = []
    return input_data

def part1(data):
    stacks = list(zip(*data[0:9]))
    filtered_stacks = []
    stack_rl = []
    for stack in stacks: #Make each stack readable
        stack_l = list(stack)
        stack_l.reverse()
        if(stack_l[0] != ' '):
            stack_rl.append(stack_l)
    for stack_e in stack_rl:
        stack_elem_l = []
        for stack_elem in stack_e:
            if not stack_elem.isspace():
                stack_elem_l.append(stack_elem)
        filtered_stacks.append(stack_elem_l) 

    filterted_commands = []
    for command in data[10:]: #Interpret commands
        command = command.split(' ')
        filterted_commands.append([int(s) for s in command if s.isdigit()])

    for command in filterted_commands: #Perform commands
        for i in range(0,command[0]):
            filtered_stacks[command[2]-1].append(filtered_stacks[command[1]-1].pop())
            
    result = ""
    for stack in filtered_stacks:
        result += stack[-1]
            
    return result

def part2(data):
    stacks = list(zip(*data[0:9]))
    filtered_stacks = []
    stack_rl = []
    for stack in stacks: #Make each stack readable
        stack_l = list(stack)
        stack_l.reverse()
        if(stack_l[0] != ' '):
            stack_rl.append(stack_l)
    for stack_e in stack_rl:
        stack_elem_l = []
        for stack_elem in stack_e:
            if not stack_elem.isspace():
                stack_elem_l.append(stack_elem)
        filtered_stacks.append(stack_elem_l) 

    filterted_commands = []
    for command in data[10:]: #Interpret commands
        command = command.split(' ')
        filterted_commands.append([int(s) for s in command if s.isdigit()])

    for command in filterted_commands: #Perform commands
        if command[0] == 1:
            filtered_stacks[command[2]-1].append(filtered_stacks[command[1]-1].pop())
        else:
            multi_operation = filtered_stacks[command[1]-1][-command[0]:]
            if len(multi_operation) != 0:
                filtered_stacks[command[2]-1].extend(multi_operation)
                for i in range(0, command[0]):
                    filtered_stacks[command[1]-1].pop()

    result = ""
    for stack in filtered_stacks:
        result += stack[-1]
            
    return result
    



if __name__ == "__main__":
    data = read_input()
    print(part1(data))
    print(part2(data))