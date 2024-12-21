import time
from aocd.models import Puzzle
from aocd import submit

DAY, YEAR = 7, 2023

def read_input():
    puzzle = Puzzle(YEAR, DAY)
    data = puzzle.input_data
    examples = puzzle.examples[0]
    return data.splitlines(), examples

def part1(data):
    for line in data:
        print(line)
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