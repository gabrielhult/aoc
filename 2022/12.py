import string

def read_input():
    with open("12.txt", "r") as f:
        input_data = f.read().split("\n")
        #Reused some stuff from day 8
        height = list(zip(*input_data))
        width = list(input_data)
        cliff_matrix = []
        root_pos = []
        for x, col in enumerate(width):
            col_l = []
            for y, char in enumerate(col):
                if(char == 'S'):
                    char = ord('a')
                    root = (x, y)
                    root_pos.append(root)
                elif(char == 'a'):
                    root_pos.append((x,y))
                    char = ord(char)
                elif(char == 'E'):
                    char = ord('z')
                    finish = (x, y)  
                else:    
                    char = ord(char)
                col_l.append(char)
            cliff_matrix.append(col_l)
        
    return cliff_matrix, root, finish, root_pos

def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
    return adjacent_indices

def part1(data, root, finish):
    exp_queue = []
    children = {}
    step_ctr = 0

    exp_queue.append(root)
    while exp_queue:
        curr_node = exp_queue.pop(0)
        if(curr_node == finish):
            while curr_node != root:
                curr_node = children[curr_node]
                step_ctr += 1
            return step_ctr
        for edge in get_adjacent_indices(curr_node[0], curr_node[1], len(data), len(data[0])):
            if(edge not in children and data[edge[0]][edge[1]] - data[curr_node[0]][curr_node[1]] <= 1):
                parent = children.get(curr_node)
                children[edge] = curr_node
                exp_queue.append(edge)
    

def part2(data, root_pos, finish):
    steps = []
    for root in root_pos:
        exp_queue = []
        children = {}
        step_ctr = 0

        exp_queue.append(root)
        while exp_queue:
            curr_node = exp_queue.pop(0)
            if(curr_node == finish):
                while curr_node != root:
                    curr_node = children[curr_node]
                    step_ctr += 1
                steps.append(step_ctr)
            for edge in get_adjacent_indices(curr_node[0], curr_node[1], len(data), len(data[0])):
                if(edge not in children and data[edge[0]][edge[1]] - data[curr_node[0]][curr_node[1]] <= 1):
                    parent = children.get(curr_node)
                    children[edge] = curr_node
                    exp_queue.append(edge)
    return min(steps)


if __name__ == "__main__":
    data, root, finish, root_pos = read_input()
    print(part1(data, root, finish))
    print(part2(data, root_pos, finish))