import time
from aocd.models import Puzzle
from aocd import submit

DAY, YEAR = 2, 2023

def read_input():
    puzzle = Puzzle(YEAR, DAY)
    data = puzzle.input_data
    examples = puzzle.examples[0]
    return data.splitlines(), examples

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
    start = time.time()
    data, examples = read_input()

    example1 = part1(examples.input_data.splitlines())
    assert int(example1) == int(examples.answer_a), f"Wrong answer. Expected {examples.answer_a}, got {example1}"
    print("\nExample1:", example1)

    part1_ans = part1(data)
    print("\nPart1:", part1_ans)
    if part1_ans is not None:
        submit(part1_ans, part="a", day=DAY, year=YEAR)

    # WIP: Might not be compatible with part2?
    # example2 = part2(examples.input_data.splitlines())
    # assert int(example2) == int(examples.answer_b), f"Wrong answer. Expected {examples.answer_b}, got {example2}"
    # print("\nExample2:", example2)

    part2_ans = part2(data)
    print("\nPart2:", part2_ans)
    if part2_ans is not None:
        submit(part2_ans, part="b", day=DAY, year=YEAR)
        
    print("Time: ", time.time() - start)