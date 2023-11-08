
def read_input():
    with open("14.txt", "r") as f:
        input_data = f.read().split("\n")
    return input_data

def print_cave(cave, y_max, x_max, x_min):
  for y in range(y_max+3):
    row = ""
    for x in range(x_min-5, x_max+6):
      if (x, y) in cave:
        row += cave[(x, y)]
      else:
        row += '.'
    print(row)
  print()

def part1(data):
    rock_paths = []
    x_min = 1000
    x_max = 0
    y_max = 0

    #Format input data
    for path in data:
        rock_coord = []
        path = path.split("->")
        for coord in path:
            coord = coord.split(",")
            coord[0], coord[1] = int(coord[0]), int(coord[1])
            if(coord[0] < x_min):
                x_min = coord[0]
            elif(coord[0] > x_max):
                x_max = coord[0]
            if(coord[1] > y_max):
                y_max = coord[1]
            rock_coord.append(coord)
        rock_paths.append(rock_coord)

    #Create appropiate 2D matrix
    cave = {}
    for x in range(x_min-1, x_max+2):
        for y in range(0, y_max+1):
            cave.update({(x,y): '.'})
        
    #Add rocks and sand spawn point to 2D matrix
    for rp in rock_paths:
        for idx, pos in enumerate(rp[:-1]):
            while True:
                cave[tuple(pos)] = '#'
                #is x coord the same?
                if(rp[idx][0] != rp[idx+1][0]):
                    if(rp[idx][0] < rp[idx+1][0]):
                        rp[idx][0] += 1
                    else:
                        rp[idx][0] -= 1
                #is y coord the same?
                elif(rp[idx][1] != rp[idx+1][1]):
                    if(rp[idx][1] < rp[idx+1][1]):
                        rp[idx][1] += 1
                    else:
                        rp[idx][1] -= 1
                else:
                    break         
    cave[(500,0)] = '+'

    start_x = 500
    start_y = 0
    curr_pos = (start_x, start_y)
    rested = 0
    
    while curr_pos[1] < y_max:
        try:
            if(cave[(curr_pos[0], curr_pos[1]+1)] == '.'):
                curr_pos = (curr_pos[0], curr_pos[1]+1)
            elif(cave[(curr_pos[0]-1, curr_pos[1]+1)] == '.'):
                curr_pos = (curr_pos[0]-1, curr_pos[1]+1)
            elif(cave[(curr_pos[0]+1, curr_pos[1]+1)] == '.'):
                curr_pos = (curr_pos[0]+1, curr_pos[1]+1)
            else:
                cave[curr_pos] = 'o'
                rested += 1
                curr_pos = (start_x, start_y)
        except KeyError as e: print("keyerror", e)

    print_cave(cave, y_max, x_max, x_min)
    return rested

def part2(data):
    rock_paths = []
    x_min = 1000
    x_max = 0
    y_max = 0

    #Format input data
    for path in data:
        rock_coord = []
        path = path.split("->")
        for coord in path:
            coord = coord.split(",")
            coord[0], coord[1] = int(coord[0]), int(coord[1])
            if(coord[0] < x_min):
                x_min = coord[0]
            elif(coord[0] > x_max):
                x_max = coord[0]
            if(coord[1] > y_max):
                y_max = coord[1]
            rock_coord.append(coord)
        rock_paths.append(rock_coord)

    #Create appropiate 2D matrix
    cave = {}
    for x in range(x_min-1, x_max+1):
        for y in range(0, y_max+3):
            print(x,y)
            cave.update({(x,y): '.'})        
        
    #Add rocks and sand spawn point to 2D matrix
    for rp in rock_paths:
        for idx, pos in enumerate(rp[:-1]):
            while True:
                cave[tuple(pos)] = '#'
                #is x coord the same?
                if(rp[idx][0] != rp[idx+1][0]):
                    if(rp[idx][0] < rp[idx+1][0]):
                        rp[idx][0] += 1
                    else:
                        rp[idx][0] -= 1
                #is y coord the same?
                elif(rp[idx][1] != rp[idx+1][1]):
                    if(rp[idx][1] < rp[idx+1][1]):
                        rp[idx][1] += 1
                    else:
                        rp[idx][1] -= 1
                else:
                    break         
    cave[(500,0)] = '+'

    start_x = 500
    start_y = 0
    curr_pos = (start_x, start_y)
    rested = 0
    
    while cave[(500, 0)] != 'o':
        if((curr_pos[0], curr_pos[1]+1) not in cave):
            cave[(curr_pos[0], curr_pos[1]+1)] = '.'
        if((curr_pos[0]-1, curr_pos[1]+1) not in cave):
            cave[(curr_pos[0]-1, curr_pos[1]+1)] = '.'
        if((curr_pos[0]+1, curr_pos[1]+1) not in cave):
            cave[(curr_pos[0]+1, curr_pos[1]+1)] = '.'

        if(cave[(curr_pos[0], curr_pos[1]+1)] == '.' and curr_pos[1] <= y_max):
            curr_pos = (curr_pos[0], curr_pos[1]+1)
        elif(cave[(curr_pos[0]-1, curr_pos[1]+1)] == '.' and curr_pos[1] <= y_max):
            curr_pos = (curr_pos[0]-1, curr_pos[1]+1)
        elif(cave[(curr_pos[0]+1, curr_pos[1]+1)] == '.' and curr_pos[1] <= y_max):
            curr_pos = (curr_pos[0]+1, curr_pos[1]+1)
        else:
            cave[curr_pos] = 'o'
            rested += 1
            curr_pos = (start_x, start_y)

    print_cave(cave, y_max, x_max, x_min)
    return rested


if __name__ == "__main__":
    data = read_input()
    print(part1(data))
    print(part2(data))