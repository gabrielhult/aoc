def read_input():
    with open("8.txt", "r") as f:
        input_data = f.read().split("\n")
    return input_data

def part1(data):
    height = list(zip(*data))
    width = list(data)
    tree_matrix = []
    for col in width:
        col_l = []
        for row in col:
            col_l.append(row)
        tree_matrix.append(col_l)
    res = 0

    row_idx = 0
    for row in tree_matrix:
        if(row_idx == 0 or row_idx == len(tree_matrix)-1):
            res += len(row)
        else:
            col_idx = 0
            for col in row:
                if(col_idx == 0 or col_idx == len(row)-1):
                    res += 1
                else:
                    #4 fall, kolla om värdena i vald riktning är mindre är den vi är på, då syns den
                    visible = False;
                    #höger
                    if(not visible):
                        idx_temp = col_idx+1
                        for next_right in tree_matrix[row_idx][idx_temp:]:
                            if(tree_matrix[row_idx][col_idx] > next_right):
                                if(idx_temp == len(row)-1):
                                    res += 1
                                    visible = True
                                    
                            else:
                                break
                            idx_temp += 1

                    #neråt
                    if(not visible):
                        idx_temp = row_idx+1
                        for next_down in tree_matrix[idx_temp:]:
                            if(tree_matrix[row_idx][col_idx] > next_down[col_idx]):
                                if(idx_temp == len(row)-1):
                                    res += 1
                                    visible = True
                            else:
                                break
                            idx_temp += 1

                    #vänster
                    if(not visible):
                        idx_temp = col_idx
                        for next_left in tree_matrix[row_idx][:idx_temp]:
                            if(tree_matrix[row_idx][col_idx] > next_left):
                                if(idx_temp-1 == 0):
                                    res += 1
                                    visible = True
                                    
                            else:
                                break
                            idx_temp -= 1

                    #uppåt
                    if(not visible):
                        idx_temp = row_idx
                        for next_up in tree_matrix[:idx_temp]:
                            if(tree_matrix[row_idx][col_idx] > next_up[col_idx]):
                                if(idx_temp-1 == 0):
                                    res += 1
                                    visible = True
                            else:
                                break
                            idx_temp -= 1

                col_idx += 1
        row_idx += 1
    return res

def part2(data):
    height = list(zip(*data))
    width = list(data)
    tree_matrix = []
    for col in width:
        col_l = []
        for row in col:
            col_l.append(row)
        tree_matrix.append(col_l)

    tree_scenery = []
    current_scenic_score = 0

    row_idx = 0
    for row in tree_matrix:
        if(row_idx == 0 or row_idx == len(tree_matrix)-1):
            print("edge filler print")
        else:
            col_idx = 0
            for col in row:
                if(col_idx == 0 or col_idx == len(row)-1):
                    print("edge filler print")
                else:
                    direction_counter = 0
                    #höger
                    if(not visible):
                        idx_temp = col_idx+1
                        for next_right in tree_matrix[row_idx][idx_temp:]:
                            if(tree_matrix[row_idx][col_idx] > next_right):
                                direction_counter += 1
                            else:
                                direction_counter += 1
                                break
                            idx_temp += 1
                    current_scenic_score = direction_counter
                    direction_counter = 0

                    #neråt
                    if(not visible):
                        idx_temp = row_idx+1
                        for next_down in tree_matrix[idx_temp:]:
                            if(tree_matrix[row_idx][col_idx] > next_down[col_idx]):
                                direction_counter += 1
                            else:
                                direction_counter += 1
                                break
                            idx_temp += 1
                    current_scenic_score = current_scenic_score * direction_counter
                    direction_counter = 0

                    #vänster
                    if(not visible):
                        idx_temp = col_idx
                        for next_left in reversed(tree_matrix[row_idx][:idx_temp]):
                            if(tree_matrix[row_idx][col_idx] > next_left):
                                direction_counter += 1
                            else:
                                direction_counter += 1
                                break
                            idx_temp -= 1
                    current_scenic_score = current_scenic_score * direction_counter
                    direction_counter = 0

                    #uppåt
                    if(not visible):
                        idx_temp = row_idx
                        for next_up in reversed(tree_matrix[:idx_temp]):
                            if(tree_matrix[row_idx][col_idx] > next_up[col_idx]):
                                direction_counter += 1
                            else:
                                direction_counter += 1
                                break
                            idx_temp -= 1
                    current_scenic_score = current_scenic_score * direction_counter
                    tree_scenery.append(current_scenic_score)
                col_idx += 1
        row_idx += 1
    return max(tree_scenery)


if __name__ == "__main__":
    data = read_input()
    print(part1(data))
    print(part2(data))