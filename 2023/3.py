import time
from aocd.models import Puzzle
from aocd import submit
import re

DAY, YEAR = 3, 2023

neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0), (1,1), (1,-1), (-1,1), (-1,-1)]

def read_input():
    puzzle = Puzzle(YEAR, DAY)
    data = puzzle.input_data
    examples = puzzle.examples[0]
    return data.split('\n'), examples

def find_nums_pos(data):
    num_to_find = []
    for y, line in enumerate(data):
        matches = re.finditer(r'\d+', line)
        temp = [(match.group(), (y, (match.start(), match.end()))) for match in matches]
        num_to_find += temp
    return num_to_find

def part1(data):
    valid_symbols = "!@#$%^&*()_-+=}[]:;/?><{|~"
    matched = []
    processed_coords = set()

    num_to_find = find_nums_pos(data)

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char in valid_symbols:
                for dx, dy in neighbours:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(line) and 0 <= ny < len(data) and data[ny][nx].isdigit() and (ny, nx) not in processed_coords:
                        for num in num_to_find:
                            num_y, (num_start_x, num_end_x) = num[1]
                            if num_y == ny and num_start_x <= nx <= num_end_x:
                                matched.append(int(num[0]))
                                processed_coords.update((ny, i) for i in range(num_start_x, num_end_x + 1))
    return sum(matched)

def part2(data):
    gear = '*'
    matched = []
    processed_coords = set()
    gear_ratio = 0

    num_to_find = find_nums_pos(data)

    for y, line in enumerate(data):
        gear_parts = 0
        for x, char in enumerate(line):
            if char in gear:
                for dx, dy in neighbours:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(line) and 0 <= ny < len(data) and data[ny][nx].isdigit() and (ny, nx) not in processed_coords:
                        for num in num_to_find:
                            num_y, (num_start_x, num_end_x) = num[1]
                            if num_y == ny and num_start_x <= nx <= num_end_x:
                                gear_parts += 1
                                matched.append(int(num[0]))
                                processed_coords.update((ny, i) for i in range(num_start_x, num_end_x + 1))
                if gear_parts != 2:
                    matched = matched[0:-gear_parts]
                else: 
                    gear_ratio += matched[-2] * matched[-1]
                gear_parts = 0
    return gear_ratio


if __name__ == "__main__":
    start = time.time()
    data, examples = read_input()

    example1 = part1(examples.input_data.split('\n'))
    assert int(example1) == int(examples.answer_a), f"Wrong answer. Expected {examples.answer_a}, got {example1}"
    print("\nExample1:", example1)

    part1_ans = part1(data)
    print("\nPart1:", part1_ans)
    if part1_ans is not None:
        submit(part1_ans, part="a", day=DAY, year=YEAR)

    example2 = part2(examples.input_data.split('\n'))
    assert int(example2) == int(examples.answer_b), f"Wrong answer. Expected {examples.answer_b}, got {example2}"
    print("\nExample2:", example2)

    part2_ans = part2(data)
    print("\nPart2:", part2_ans)
    if part2_ans is not None:
        submit(part2_ans, part="b", day=DAY, year=YEAR)
        
    print("Time: ", time.time() - start)