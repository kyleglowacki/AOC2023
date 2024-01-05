import copy

# BOILER PLATE
def load_file():
    name = "day23_2023.txt"
    with open(name, "r") as f:
        data = f.read()
        data = data.splitlines()

    return data

def write_to_file(i, lines):
    name = f"day23_2023_{i}.txt"
    with open(name, "w") as f:
        for line in lines:
            for item in line:
                f.write(f"{item}")
            f.write("\n")

def convert_to_list(lines):
    data = []
    for line in lines:
        elems = [*line]
        data.append(elems)
    return data

def cnt_data(data, val):
    amt = 0
    for d in data:
        for i in d:
            if i == val:
                amt += 1
    return amt

def make_grid(rows, cols, val):
    grid = []
    for row in range(rows):
        grid.append([val] * cols)
    return grid

def add_to_db(bdb, kv):
    try:
        old = bdb[kv]
        return False, bdb
    except KeyError:
        bdb[kv] = True
        return True, bdb

# list of string
def copy_grid(orig):
    new_grid = []
    for item in orig:
        new_grid.append(item)
    return new_grid
        
    
##
##  DAY SPECIFIC
##
def parse(data):
    d = []
    for line in data:
        d.append([])
        for char in line:
            d[-1].append(char)
    return d

def valid_step(data,r2,c2):
    if (r2 < 0) or (c2 < 0):
        return False
    if (r2 >= len(data)) or (c2 >= len(data[0])):
        return False

    #print(f"Looking at {r2},{c2} {data[r2][c2]}")

    # Don't let us move the wrong way at the last choice
    if data[r2][c2] == "#":
        return False
    if data[r2][c2] == ".":
        return True
    if (data[r2][c2] == "<") or (data[r2][c2] == ">"):
        return True
    if (data[r2][c2] == "v") or (data[r2][c2] == "^"):
        return True

    print("UNEXPECTED")
    return False

def add_hash(d,r,c):
    return d[r][:c] + "#" + d[r][c+1:]

def take_step(pos):
    step = pos[3]+1
    # NESW
    dir = [[-1,0], [0,1], [1,0], [0,-1]]
    #print(f"Taking step {step} from {pos[0]},{pos[1]}")
    next = []
    # Check each item with the current step number
    r1 = pos[0]
    c1 = pos[1]

    for d in dir:
        #print(f"Check direction {d} from {r1},{c1}")
        r2 = r1+d[0]
        c2 = c1+d[1]
        if valid_step(pos[2], r2, c2):
            #print(f"Found valid direction {d}")
            pos[2][r2] = add_hash(pos[2], r2, c2)
            return [r2, c2, pos[2], step]
    print(f"UNEXPECTED")
    return []

def at_exit(cur):
    xx = len(cur[2])-1
    xy = len(cur[2][0])-2
    return (cur[0] == xx) and (cur[1] == xy)


def find_spots(data, lim):
    dir = [[-1,0], [0,1], [1,0], [0,-1]]
    intersections = []
    for r,line in enumerate(data):
        for c,spot in enumerate(line):
            cnt = 0
            if data[r][c] != "#":
                for d in dir:
                    r2 = r+d[0]
                    c2 = c+d[1]
                    if valid_step(data, r2, c2):
                        cnt += 1
                if cnt == lim:
                    intersections.append([r,c])
    return intersections

def is_intersection(data, r, c):
    cnt = 0
    dir = [[-1,0], [0,1], [1,0], [0,-1]]
    for d in dir:
        r2 = r+d[0]
        c2 = c+d[1]
        if valid_step(data, r2, c2):
            cnt += 1
    return cnt > 2

def is_in_intersection_list(i, r, c):
    for idx, item in enumerate(i):
        if item[0] == r and item[1] == c:
            return True
    return False

def create_blank_connections(intersections):
    connection = {}
    dummy = {"nodes": [], "dist": []}
    for idx, item in enumerate(intersections):
        connection[idx] = copy.deepcopy(dummy)
    return connection

def match_intersection(i,r,c):
    for idx, item in enumerate(i):
        if item[0] == r and item[1] == c:
            return idx
    print(f"Unable to find {r},{c} in {i}")
    return 0

def find_path_length(data, r1, c1, r2, c2, i):
    d = copy_grid(data)
    # Mark start position
    d[r1] = add_hash(d, r1, c1)
    d[r2] = add_hash(d, r2, c2)
    next = [r2, c2, d, 1]
    while not is_in_intersection_list(i, next[0], next[1]):
        #print(f"Stepping away from {next[0]},{next[1]}")
        next = take_step(next)
    #print(f"Arrived at intersection {next[0]},{next[1]}")
    steps  = next[3]
    idx = match_intersection(i,next[0],next[1])
    return steps, idx

# data, intersections, index into intersections, connections
def figure_out_paths(d, i, idx, c):
    r1 = i[idx][0]
    c1 = i[idx][1]
    dir = [[-1,0], [0,1], [1,0], [0,-1]]
    for d in dir:
        r2 = r1+d[0]
        c2 = c1+d[1]
        if valid_step(data, r2, c2):
            #print(f"Path away from {r1},{c1} towards {d}")
            # Get the distance and intex of the intersection at
            # the end of the path
            path_len, corner_index = find_path_length(data, r1, c1, r2, c2, i)
            # Update c to add dist and node
            nodes = c[idx]["nodes"]
            dist = c[idx]["dist"]
            nodes.append(corner_index)
            dist.append(path_len)
            c[idx]["nodes"] = nodes
            c[idx]["dist"] = dist
    return c

def walk_maze(data, intersections):
    # Build mapping (nodes #s are intersection index)
    # {1: {"nodes" : [2,3,4], "dist" : [18, 22, 5]},
    #  2: ....
    connection = create_blank_connections(intersections)

    for idx, item in enumerate(intersections):
        # Figure out nodes this intersection connects to
        # and the distances
        #print(f"Figure out paths from {item}")
        connection = figure_out_paths(data, intersections, idx, connection)
    return connection

def get_dist(c, start, stop):
    n = c[start]["nodes"]
    d = c[start]["dist"]
    for idx, item in enumerate(n):
        if item == stop:
            return d[idx]
    print("UNEXPECTED")
    return 0



def keep_best(old, b):
    if len(old) == 0:
        return b
    print(f"Consider longest path {old[0]} vs {b[0]}")
    print(f"Consider longest path {old[1]} vs {b[1]}")
    if old[0] < b[0]:
        print(f"Picking {b[0]}")
        return b
    else:
        print(f"Picking {old[0]}")
        return old

final_paths = []
    
def find_longest_path(c, stop, paths):
    global final_paths

    updated_paths = []
    
    for path in paths:
        start = path[-1]
        # Where current node connects
        nodes = c[start]["nodes"]

        # Create more paths
        for idx, node in enumerate(nodes):
            dist_to_node = c[start]["dist"][idx]
            if node == stop:
                # We made it
                new_path = copy.deepcopy(path)
                new_path[0] += dist_to_node
                new_path.append(node)
                # save off answer
                final_paths.append(new_path)
                print(f"THE END {new_path}")
            elif not node in path:
                #print(f"Node {node} is not in path = {path}")
                # Generate new paths and append
                new_path = copy.deepcopy(path)
                new_path[0] += dist_to_node
                new_path.append(node)
                # save off answer
                updated_paths.append(new_path)
            # else
            # no valid steps.. so don't copy into updated_paths

    if len(updated_paths) > 0:
        find_longest_path(c, stop, updated_paths)

def find_max_path(fp):
    mx = fp[0]
    for path in fp:
        if path[0] > mx[0]:
            mx = path
    return mx

# REAL DATA
data = load_file()
# SAMPLE DATA
data2 = ["#.#####################",
        "#.......#########...###",
        "#######.#########.#.###",
        "###.....#.>.>.###.#.###",
        "###v#####.#v#.###.#.###",
        "###.>...#.#.#.....#...#",
        "###v###.#.#.#########.#",
        "###...#.#.#.......#...#",
        "#####.#.#.#######.#.###",
        "#.....#.#.#.......#...#",
        "#.#####.#.#.#########v#",
        "#.#...#...#...###...>.#",
        "#.#.#v#######v###.###v#",
        "#...#.>.#...>.>.#.###.#",
        "#####v#.#.###v#.#.###.#",
        "#.....#...#...#.#.#...#",
        "#.#########.###.#.#.###",
        "#...###...#...#...#.###",
        "###.###.#.###v#####v###",
        "#...#...#.#.>.>.#.>.###",
        "#.###.###.#.###.#.#v###",
        "#.....###...###...#...#",
        "#####################.#"]

# Convert to list
#data = parse(data)

cnt = 0
for line in data:
    cnt += line.count(".")


print(f"Maximum possible steps = {cnt-1}")

intersections = find_spots(data,1)
#print(f"Start / Stop points = {len(intersections)}")
#print(intersections)
intersections += find_spots(data,3)
#print(f"Add in 3 direction intersections, now we have {len(intersections)}")
#print(intersections)
intersections += find_spots(data,4)
#print(f"Add in 4 direction intersections, now we have {len(intersections)}")
print(intersections)

# Walk maze and populate distances / connect intersections
connections = walk_maze(data, intersections)
print(f"Connections = {connections}")

find_longest_path(connections, 18, [[109,0,4]])
print(f"Paths = {len(final_paths)}")

mx = find_max_path(final_paths)
print(f"Longest Path Dist = {mx[0]}+81")
print(f"Longest Path Nodes = {mx[1:]}")

# 6684 too high
# 6685 too high
#Paths = 1262816
#Longest Path Dist = 6646
#Longest Path Nodes = [0, 4, 7, 9, 12, 13, 16, 15, 17, 35, 28, 30, 34, 33, 31, 24, 26, 25, 20, 21, 23, 2, 5, 3, 6, 8, 22, 27, 29, 11, 14, 32, 19, 18, 1]
