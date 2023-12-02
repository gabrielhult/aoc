def read_input():
    with open("2023/2.txt", "r") as f:
        input_data = f.read().split("\n")
    return input_data

def part1(data):
    mr = 12
    mg = 13
    mb = 14
    id_sum = 0
    for game in data:
        curr_r = curr_g = curr_b = 0
        gid = int(game.split(':')[0].split()[1])
        game = game.split(':')[1].split('; ')
        for game_set in game:
            for n, color in map(str.split, game_set.split(', ')):
                if color == "red" and int(n) > curr_r :
                    curr_r = int(n)
                elif color == "green" and int(n) > curr_g :
                    curr_g = int(n)
                elif color == "blue" and int(n) > curr_b :
                    curr_b = int(n)
        if curr_r <= mr and curr_g <= mg and curr_b <= mb:
            id_sum += gid
    return id_sum

def part2(data):
    res = 0
    for game in data:
        minred = mingreen = minblue = 0
        curr_r = curr_g = curr_b = 0
        game = game.split(':')[1].split('; ')
        for game_set in game:
            for n, color in map(str.split, game_set.split(', ')):
                if color == "red" and int(n) > curr_r :
                    curr_r = int(n)
                elif color == "green" and int(n) > curr_g :
                    curr_g = int(n)
                elif color == "blue" and int(n) > curr_b :
                    curr_b = int(n)
            minred = max(curr_r, minred)
            mingreen = max(curr_g, mingreen)
            minblue = max(curr_b, minblue)
        res += minred * mingreen * minblue
    return res


if __name__ == "__main__":
    data = read_input()
    print(part1(data))
    print(part2(data))