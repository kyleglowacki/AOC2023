# BOILER PLATE
def load_file():
    name = "day18_2023.txt"
    with open(name, "r") as f:
        data = f.read()
        data = data.splitlines()

    return data

def write_to_file(i, lines):
    name = f"day18_2023_{i}.txt"
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

##
##  DAY SPECIFIC
##

def process(g, inst, x, y):
    minx = 3000
    maxx = 0
    miny = 3000
    maxy = 0

    for i in inst:
    
        d = {"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}
        #print(i)

    
        for s in range(i[1]):
            x += d[i[0]][0]
            y += d[i[0]][1]
            
            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, x)
            maxy = max(maxy, y)
        
            g[x][y] = 1

    print(f"{minx} to {maxx}, {miny} to {maxy}")
        
    return g, x, y

def spread(grid, val):
    d = {"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}
    cnt = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == val:
                for r in d:
                    #print(d[r])
                    if grid[row+d[r][0]][col+d[r][1]] == 0:
                        grid[row+d[r][0]][col+d[r][1]] = 2
                        cnt += 1
    print(f"Spreading {cnt}")
    return grid, cnt == 0


data = load_file()
data2 = ["R 6 (#70c710)",
        "D 5 (#0dc571)",
        "L 2 (#5713f0)",
        "D 2 (#d2c081)",
        "R 2 (#59c680)",
        "D 2 (#411b91)",
        "L 5 (#8ceee2)",
        "U 2 (#caa173)",
        "L 1 (#1b58a2)",
        "U 2 (#caa171)",
        "R 2 (#7807d2)",
        "U 3 (#a77fa3)",
        "L 2 (#015232)",
        "U 2 (#7a21e3)"]
inst = []
for line in data:
    dir, mag, color = line.split()
    inst.append([dir, int(mag)])

grid = make_grid(700,700,0)
    
# FIRST
posx = 300
posy = 300
#posx = 10
#posy = 10

grid, posx, posy = process(grid, inst, posx, posy)

grid[270][115] = 2
#grid[11][11] = 2
done = False

write_to_file(0, grid)

while not done:
    grid, done = spread(grid, 2)

print(f"Count of edge {cnt_data(grid, 1)}")
print(f"Count of inside {cnt_data(grid, 2)}")
    
print(f"FIRST Total = {total}")


# SECOND

