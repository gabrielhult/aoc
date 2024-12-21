import time
from aocd.models import Puzzle
from aocd import submit
import re

DAY, YEAR = 5, 2023

def read_input():
    puzzle = Puzzle(YEAR, DAY)
    data = puzzle.input_data
    examples = puzzle.examples[0]
    return data.splitlines(), examples

def part1(data):
    seeds = [int(seed) for seed in re.findall(r'\d+', data[0])]
    almanac = [[int(num) for num in re.findall(r'\d+', line)] for line in data[1:] if len(line) != 0]
    
    print(almanac, seeds)
    # fixed_almanac = []
    # final_almanac = []
    # is_next = True
    # for i, row in enumerate(almanac):
    #     if len(row) == 0 and is_next:
    #         fixed_almanac.append([])
    #         is_next = False
    #     if len(row) != 0:
    #         row = [int(row[j]) for j in range(len(row))]
    #         row_to_map = {row[1]+j: row[0]+j for j in range(0, row[2]) }
    #         print(row_to_map)
    #         fixed_almanac.append(row_to_map)
    #         is_next = True
    # for elem in fixed_almanac:
    #     if elem != []:
    #         pass
    # print(fixed_almanac)
    return

def part2(data):
    return


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
    assert int(example2) == int(examples.answer_b), f"Wrong answer. Expected {examples.answer_b}, got {example2}"
    print("\nExample2:", example2)

    part2_ans = part2(data)
    print("\nPart2:", part2_ans)
    if part2_ans is not None:
        submit(part2_ans, part="b", day=DAY, year=YEAR)
        
    print("Time: ", time.time() - start)