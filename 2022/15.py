def read_input():
    with open("15.txt", "r") as f:
        input_data = f.read().split("\n")
    return input_data

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]-1:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

def part1(data):
    sensor_poses = []
    beacon_poses = []
    manh_dists = []
    x_min = 1000
    x_max = 0
    y_min = 1000
    y_max = 0

    for row in data:
        sensorx = int(row.split(':')[0].split(", ")[0][12:])
        sensory = int(row.split(':')[0].split(", ")[1][2:])
        beaconx = int(row.split(':')[1].split(", ")[0].split("at ")[1][2:])
        beacony = int(row.split(':')[1].split(", ")[1][2:])
        
        manh_dist = abs(sensorx-beaconx) + abs(sensory-beacony)
        if(sensorx < x_min + manh_dist):
            x_min = sensorx - manh_dist
        elif(sensorx > x_max - manh_dist):
            x_max = sensorx + manh_dist

        if(sensory < y_min + manh_dist):
            y_min = sensory - manh_dist
        elif(sensory > y_max - manh_dist):
            y_max = sensory + manh_dist

        sensor_pos = (sensorx, sensory)
        beacon_pos = (beaconx, beacony)
        sensor_poses.append(sensor_pos)
        beacon_poses.append(beacon_pos)
        manh_dists.append(manh_dist)
    
    desired_y = 2000000
    
    desired_intervals = []
    for idx, sensor in enumerate(sensor_poses):
        dist = manh_dists[idx]
        dist_des_y = abs(desired_y - sensor[1])
        if(dist >= dist_des_y):
            interval_border = dist - dist_des_y
            desired_intervals.append([sensor[0]-interval_border, sensor[0]+interval_border])
    merged = merge_intervals(desired_intervals)
    res = merged[0][1] - merged[0][0]
    return res

def part2(data):
    sensor_poses = []
    beacon_poses = []
    manh_dists = []
    x_min = 0
    x_max = 4000000
    y_min = 0
    y_max = 4000000

    for row in data:
        sensorx = int(row.split(':')[0].split(", ")[0][12:])
        sensory = int(row.split(':')[0].split(", ")[1][2:])
        beaconx = int(row.split(':')[1].split(", ")[0].split("at ")[1][2:])
        beacony = int(row.split(':')[1].split(", ")[1][2:])
        manh_dist = abs(sensorx-beaconx) + abs(sensory-beacony)

        sensor_pos = (sensorx, sensory)
        beacon_pos = (beaconx, beacony)
        sensor_poses.append(sensor_pos)
        beacon_poses.append(beacon_pos)
        manh_dists.append(manh_dist)

    for y in range(0, y_max+1):
        desired_intervals = []
        for idx, sensor in enumerate(sensor_poses):
            dist = manh_dists[idx]
            dist_des_y = abs(y - sensor[1])
            if(dist >= dist_des_y):
                interval_border = dist - dist_des_y
                desired_intervals.append([sensor[0]-interval_border, sensor[0]+interval_border])
        merged = merge_intervals(desired_intervals)
        if(len(merged) > 1):
            x = merged[1][0] - 1
            res = (x, y)
            break
    distress_signal = res[0] * 4000000 + res[1]

    print(res) #för skojs skull
    return distress_signal


if __name__ == "__main__":
    data = read_input()
    print(part1(data))
    print(part2(data))