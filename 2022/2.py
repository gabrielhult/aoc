def read_input():
    with open("2.txt", "r") as f:
        input_data = f.read().split("\n")
    return input_data

def part1(data):
    score = 0
    for game in data:
        if game[0] == 'A':
            if game[-1] == 'X':
                score += 4
            elif game[-1] == 'Y':
                score += 8
            elif game[-1] == 'Z':
                score += 3

        elif game[0] == 'B':
            if game[-1] == 'X':
                score += 1
            elif game[-1] == 'Y':
                score += 5
            elif game[-1] == 'Z':
                score += 9

        elif game[0] == 'C':
            if game[-1] == 'X':
                score += 7
            elif game[-1] == 'Y':
                score += 2
            elif game[-1] == 'Z':
                score += 6

    return score

def part2(data):
    score = 0
    for game in data:
        if game[0] == 'A':
            if game[-1] == 'X':
                score += 3
            elif game[-1] == 'Y':
                score += 4
            elif game[-1] == 'Z':
                score += 8

        elif game[0] == 'B':
            if game[-1] == 'X':
                score += 1
            elif game[-1] == 'Y':
                score += 5
            elif game[-1] == 'Z':
                score += 9

        elif game[0] == 'C':
            if game[-1] == 'X':
                score += 2
            elif game[-1] == 'Y':
                score += 6
            elif game[-1] == 'Z':
                score += 7
    return score






if __name__ == "__main__":
    data = read_input()
    print(part1(data))
    print(part2(data))