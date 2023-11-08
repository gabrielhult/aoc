def read_input():
    with open("10.txt", "r") as f:
        input_data = f.read().split("\n")
    return input_data

def part1(data):
    reg_x = 1
    interesting_cycles = [20, 60, 100, 140, 180, 220]
    signal_strenths = []
    cycle_counter = 0
    for instr in data:
        if(instr[0:4] == "noop"):
            cycle_counter += 1
            if(cycle_counter in interesting_cycles):
                signal_strenths.append(cycle_counter*reg_x)
        else:
            addx, val = instr.split(" ")
            for i in range(2):
                cycle_counter += 1
                if(cycle_counter in interesting_cycles):
                    signal_strenths.append(cycle_counter*reg_x)
                if(i == 1): #second cycle
                    reg_x += int(val)
    return sum(signal_strenths)

def part2(data):
    reg_x = 1
    reg_x_top = reg_x + 2
    cycle_counter = 0
    crt = ""
    crt_counter = 1
    for instr in data:
        if(instr[0:4] == "noop"):
            if(cycle_counter % 40 == 0 and cycle_counter != 0):
                crt += '\n'
                crt_counter -= 40
            cycle_counter += 1

            if(reg_x <= crt_counter <= reg_x_top):
                crt += '#'
            else:
                crt += '.'
            crt_counter += 1
        else:
            addx, val = instr.split(" ")
            for i in range(2):
                if(cycle_counter % 40 == 0 and cycle_counter != 0):
                    crt += '\n'
                    crt_counter -= 40
                cycle_counter += 1
                
                if(reg_x <= crt_counter <= reg_x_top):
                    crt += '#'
                else:
                    crt += '.'
                crt_counter += 1
                
                if(i == 1): #second cycle
                    reg_x += int(val)
                    reg_x_top += int(val)
        
    return crt


if __name__ == "__main__":
    data = read_input()
    print(part1(data))
    print(part2(data))