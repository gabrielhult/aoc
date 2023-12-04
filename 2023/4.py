import time
from aocd.models import Puzzle
from aocd import submit
import re

DAY, YEAR = 4, 2023

def read_input():
    puzzle = Puzzle(YEAR, DAY)
    data = puzzle.input_data
    examples = puzzle.examples[0]
    return data.splitlines(), examples

def part1(data):
    w_num = [re.findall(r'\d+', game.split(":")[1].split("|")[0]) for game in data]
    my_nums = [re.findall(r'\d+', game.split(":")[1].split("|")[1]) for game in data]
    tot = 0
    for i, game in enumerate(w_num):
        matches = 0
        for num in my_nums[i]:
            if num in game:
                if matches == 0:
                    matches += 1
                else:
                    matches *= 2
        tot += matches
    return tot

def part2(data):
    w_num = [re.findall(r'\d+', game.split(":")[1].split("|")[0]) for game in data]
    my_nums = [re.findall(r'\d+', game.split(":")[1].split("|")[1]) for game in data]
    instance_factor = [1 for game in data]
    tot = 0
    for i, game in enumerate(w_num):
        matches = 0
        for num in my_nums[i]:
            if num in game:
                matches += 1
        for j in range(matches):
            instance_factor[i+j+1] += instance_factor[i]
    tot = sum(instance_factor)
    return tot


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

    # Works if same example data is used for both parts
    example2 = part2(examples.input_data.splitlines())
    #assert example2 == int(examples.answer_b), f"Wrong answer. Expected {examples.answer_b}, got {example2}"
    print("\nExample2:", example2)

    part2_ans = part2(data)
    print("\nPart2:", part2_ans)
    if part2_ans is not None:
        submit(part2_ans, part="b", day=DAY, year=YEAR)
        
    print("Time: ", time.time() - start)