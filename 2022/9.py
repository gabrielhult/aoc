import math

def read_input():
    with open("9.txt", "r") as f:
        input_data = f.read().split("\n")
    return input_data

def part1(data):
    visited = [[0,0]] #the only element from the start, s
    head_pos = [0, 0]
    tail_pos = [0, 0]

    dir_dict = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]} #x, y

    for command in data:
        direction, steps = command.split(" ")
        for step in range(int(steps)):
            move_tail = False
            head_pos = [sum(x) for x in zip(head_pos, dir_dict.get(direction))]

            if(head_pos[0] >= tail_pos[0] + 2):
                move_tail = True
                tail_pos = [head_pos[0]-1, head_pos[1]]

            elif(head_pos[0] <= tail_pos[0] - 2):
                move_tail = True
                tail_pos = [head_pos[0]+1, head_pos[1]]

            elif(head_pos[1] >= tail_pos[1] + 2):
                move_tail = True
                tail_pos = [head_pos[0], head_pos[1]-1]

            elif(head_pos[1] <= tail_pos[1] - 2):
                move_tail = True
                tail_pos = [head_pos[0], head_pos[1]+1]

            if(move_tail):
                if(tail_pos not in visited):
                    visited.append(tail_pos)
    return len(visited)

def part2(data):
    visited = [set() for i in range(10)]
    rope = [0] * 10
    sign = lambda x: 1 if x>0 else -1 if x<0 else 0 #ChatGPT shout-out

    dir_dict = {'R': 1, 'L': -1, 'U': 1j, 'D': -1j} #x, y in list was bruh in part 2, complex worked better

    for command in data:
        direction, steps = command.split(" ")
        for step in range(int(steps)):
            move_tail = False
            rope[0] += dir_dict.get(direction)
            for i in range(1,10):
                dist = rope[i-1] - rope[i]
                if(abs(dist) >= 2):
                    rope[i] += complex(sign(dist.real), sign(dist.imag))
                visited[i].add(rope[i])    
    return len(visited[-1])


if __name__ == "__main__":
    data = read_input()
    print(part1(data))
    print(part2(data))