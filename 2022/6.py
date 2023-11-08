def read_input():
    with open("6.txt", "r") as f:
        input_data = f.read().split("\n")
    return input_data

def part1(data):
    res = 0
    cs: str = ""
    for letter in data[0]:
        if len(cs) >= 4:
            cs = cs[1:]
            cs += letter
            if(len(set(cs)) == len(cs)):
                res += 1
                break
        else:
            cs += letter   
        res += 1     
    return res

def part2(data):
    res = 0
    cs: str = ""
    for letter in data[0]:
        if len(cs) >= 14:
            cs = cs[1:]
            cs += letter
            if(len(set(cs)) == len(cs)):
                res += 1
                break
        else:
            cs += letter   
        res += 1
    return res


if __name__ == "__main__":
    data = read_input()
    print(part1(data))
    print(part2(data))