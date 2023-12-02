import time
from aocd.models import Puzzle
from aocd import submit

DAY, YEAR = 0, 2023

def read_input():
    puzzle = Puzzle(YEAR, DAY)
    data = puzzle.input_data
    return data.splitlines()

def part1(data):
    return

def part2(data):
    return


if __name__ == "__main__":
    start = time.time()
    data = read_input()

    part1_ans = part1(data)
    print("\nPart1:", part1_ans)
    if part1_ans is not None:
        submit(part1_ans, part="a", day=DAY, year=YEAR)

    part2_ans = part2(data)
    print("\nPart2:", part1_ans)
    if part2_ans is not None:
        submit(part2_ans, part="a", day=DAY, year=YEAR)
        
    print("Time: ", time.time() - start)