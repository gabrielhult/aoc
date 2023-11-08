def read_input():
    with open("readme", "r") as f:
        input_data = f.read().split("\n")
        print(input_data)
    return input_data

def part1(data):
    return

def part2(data):
    return


if __name__ == "__main__":
    data = read_input()
    print(part1(data))
    print(part2(data))