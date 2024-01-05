
def load_file():
    name = "day21_2023.txt"
    with open(name, "r") as f:
        data = f.read()
        data = data.splitlines()

    return data

def write_to_file(i, lines):
    name = f"day21_2023_{i}.txt"
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

def mark(steps, row, col, val):
    dirs = [[-1,0],[1,0],[0,-1],[0,1]]
    cnt = 0
    for d in dirs:
        try:
            if (row+d[0] >= 0) and (col+d[1] >= 0):
                if steps[row+d[0]][col+d[1]] != '#':
                    steps[row+d[0]][col+d[1]] = val
        
        except IndexError as e:
            pass
    return steps

def do_steps(steps, current):
    val = current
    next = 1
    if current != 'S':
        val = int(current)
        next = val + 1
        
    for row in range(len(steps)):
        for col in range(len(steps[row])):
            if steps[row][col] == val:
                steps = mark(steps, row, col, next)
    return steps

def cnt_data(data, val):
    amt = 0
    for d in data:
        for i in d:
            if i == val:
                amt += 1
    return amt
                
data = ["...........",
        ".....###.#.",
        ".###.##..#.",
        "..#.#...#..",
        "....#.#....",
        ".##..S####.",
        ".##..#...#.",
        ".......##..",
        ".##.#.####.",
        ".##..##.##.",
        "..........."]
data = load_file()


# FIRST
total = 0
stepped = convert_to_list(data)
stepped = do_steps(stepped, 'S')
write_to_file(1, stepped)
for i in range(2,70):
    stepped = do_steps(stepped, i-1)
    step_nums = cnt_data(stepped, i)
    write_to_file(i, stepped)
    print(f"Marked {step_nums} for step {i}")

print(f"FIRST Total = {step_nums}")
# 261 too small
# 11451 too high
# 11981 too high
# SECOND

