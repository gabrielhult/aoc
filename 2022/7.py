
res_sum1 = 0
max_space = 70000000
update_size = 30000000
all_dir_sizes = []

def read_input():
    with open("7.txt", "r") as f:
        input_data = f.read().split("\n")
    return input_data

def part1(data):
    global res_sum1
    size = 0
    
    while(len(data) > 0):
        if(data[0][0:7] == "$ cd .."):
            
            if(size <= 100000):
                res_sum1 += size
            data.pop(0)
            break

        else:
            if(data[0][0] == "$"):
                if(data[0][0:4] == "$ cd"):
                    data.pop(0)
                    size += part1(data)
                elif(data[0][0:4] == "$ ls"):
                    data.pop(0)
                    while (len(data) > 0 and data[0][0] != "$"):
                        if(data[0][0] != "d"):
                            size += int(data[0].split(" ")[0])
                        data.pop(0)
    all_dir_sizes.append(size) #added for part 2
    return size

def part2(data):
    space_left = max_space - max(all_dir_sizes)
    space_required = update_size - space_left
    min_size = None
    for dir_size in all_dir_sizes:            
        if(dir_size >= space_required):
            if(min_size == None):
                min_size = dir_size
            elif(dir_size < min_size and min_size != None):
                min_size = dir_size

    return min_size


if __name__ == "__main__":
    data = read_input()
    part1(data)
    print(res_sum1)
    print(part2(data))