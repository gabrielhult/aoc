import time
from aocd.models import Puzzle
from aocd import submit

DAY, YEAR = 1, 2023

def read_input():
    puzzle = Puzzle(YEAR, DAY)
    data = puzzle.input_data
    return data.splitlines()

def part1(data):
    res = 0
    for word in data:
        word_sum = ''
        for char in word:
            if char.isdigit():
                word_sum += char
        word_sum = int(word_sum[0] + word_sum[-1])
        res += word_sum
    return res

def part2(data):
    word_to_num = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }  
    res = 0
    for word in data:
        word_sum = 0
        nums = []
        for i, char in enumerate(word):
            if char.isdigit():
                nums.append((i, char))
        for key in word_to_num:
            for i, char in enumerate(word):
                if word[i:i+len(key)] == key:
                    nums.append((i, word_to_num[key]))
        nums.sort() 
        word_sum = int(nums[0][1] + nums[-1][1])
        res += word_sum
    return res


if __name__ == "__main__":
    start = time.time()
    data = read_input()

    part1_ans = part1(data)
    print("\nPart1:", part1_ans)
    if part1_ans is not None:
        submit(part1_ans, part="a", day=DAY, year=YEAR)

    part2_ans = part2(data)
    print("\nPart2:", part2_ans)
    if part2_ans is not None:
        submit(part2_ans, part="a", day=DAY, year=YEAR)
        
    print("Time: ", time.time() - start)