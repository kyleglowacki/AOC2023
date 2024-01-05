def LoadFile():
    name = "day08_2023.txt"
    with open(name, "r") as f:
        data = f.read()
        data = data.splitlines()

    inst = data[0]
    maze = {}
    start_list = []
    end_list = []
    for line in data[2:]:
        k = line[0:3]
        l = line[7:10]
        r = line[12:15]
        sub_dict = {"L": l, "R": r}
        maze[k] = sub_dict

        if line[2] == "A":
            start_list.append(k)
        if (line[2] == "Z"):
            end_list.append(k)
        if (line[9] == "Z"):
            end_list.append(l)
        if (line[14] == "Z"):
            end_list.append(r)

    start_list = list(set(start_list))
    end_list = list(set(end_list))
    return inst, maze, start_list, end_list

ans = []
inst, maze, start_list, end_list = LoadFile()
# FIRST
done = False
next_inst = 0
steps = 0
current = "AAA"
while not done:

    steps += 1

    direction = inst[next_inst]
    choices = maze[current]

    new_location = choices[direction]
    #print(f"Going {direction} from {current} to {new_location} on step {steps}")
    
    if new_location == "ZZZ":
        done = True
    else:
        current = new_location
        next_inst += 1
        if next_inst == len(inst):
            next_inst = 0

print(f"Part 1 - Steps {steps}")
            
# SECOND
print(f"Start List - {start_list}")
print(f"End List - {end_list}")

current = start_list
done = False
steps = 0
next_inst = 0
while not done:

    steps += 1
    found = 0
    new_location = []

    for item in current:
    
        direction = inst[next_inst]
        choices = maze[item]
        
        new_location.append(choices[direction])
        #print(f"Going {direction} from {item} to {choices[direction]} on step {steps}")
    
        if choices[direction] in end_list:
            print(f"Path {len(new_location)} located an endpoint at {choices[direction]} on step {steps}")
            found += 1
            

    if found > 0:
        print(f"{found} of 6 reached the end on {steps}")
    if found == len(end_list):
        done = True
        
    current = new_location
    next_inst += 1
    if next_inst == len(inst):
        next_inst = 0

print(f"Part 2 - Steps {steps}")

# Path 1 every 12361
# Path 2 every 16043
# Path 3 every 18673
# Path 4 every 19199
# Path 5 every 13939
# Path 6 every 11309
import math
math.lcm(12361, 16043, 18673, 19199, 13939, 11309)
