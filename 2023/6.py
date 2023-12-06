import time
from aocd.models import Puzzle
from aocd import submit
import re

DAY, YEAR = 6, 2023

def read_input():
    puzzle = Puzzle(YEAR, DAY)
    data = puzzle.input_data
    examples = puzzle.examples[0]
    return data.splitlines(), examples

def part1(data):
    times = [int(i) for i in re.findall(r'\d+', data[0])]
    distances = [int(i) for i in re.findall(r'\d+', data[1])]
    record_factor = 0

    for i, time in enumerate(times):
        record_counter = 0
        for j in range(0, time+1): # How many milliseconds the "button is pressed"
            if j != 0 and j != time:
                drive_time = time - j
                distance = j * drive_time
                if distance > distances[i]:
                    record_counter += 1
        if record_factor == 0:
            record_factor = record_counter
        else:
            record_factor *= record_counter
    return record_factor

def part2(data):
    time = int(''.join(re.findall(r'\d+', data[0])))
    distance = int(''.join(re.findall(r'\d+', data[1])))
    record_counter = 0
    for j in range(0, time+1): # How many milliseconds the "button is pressed"
        if j != 0 and j != time:
            drive_time = time - j
            new_dist = j * drive_time
            if new_dist > distance:
                record_counter += 1
    return record_counter


if __name__ == "__main__":
    start = time.time()
    data, examples = read_input()

    # example1 = part1(examples.input_data.splitlines())
    # assert int(example1) == int(examples.answer_a), f"Wrong answer. Expected {examples.answer_a}, got {example1}"
    # print("\nExample1:", example1)

    part1_ans = part1(data)
    print("\nPart1:", part1_ans)
    if part1_ans is not None:
        submit(part1_ans, part="a", day=DAY, year=YEAR)

    # # Works if same example data is used for both parts
    # example2 = part2(examples.input_data.splitlines())
    # assert int(example2) == int(examples.answer_b), f"Wrong answer. Expected {examples.answer_b}, got {example2}"
    # print("\nExample2:", example2)

    part2_ans = part2(data)
    print("\nPart2:", part2_ans)
    if part2_ans is not None:
        submit(part2_ans, part="b", day=DAY, year=YEAR)
        
    print("Time: ", time.time() - start)