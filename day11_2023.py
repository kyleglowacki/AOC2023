
def load_file():
    name = "day11_2023.txt"
    with open(name, "r") as f:
        data = f.read()
        data = data.splitlines()

    return data

def expand_galaxy(data):
    # Expand y
    blank_row = "." * len(data[0])
    new_galaxy = []
    for y in range(len(data)):
        if data[y].find('#') == -1:
            print(f"Expand Blank Line at row {y}")
            new_galaxy.append(blank_row)
            new_galaxy.append(blank_row)
        else:
            #print(f"Non-Blank Line at row {y}")            
            new_galaxy.append(data[y])

    data = new_galaxy
    #print(data)
    x = len(data[0])-1
    # start at the lines so when it expands we don't risk duplicating
    #print(f"LEN of data = {x}")
    while x > 0:

        found = False
        for y in range(len(data)):
            if data[y][x] == '#':
                #print(f"Found galaxy in column {x}")
                found = True
        if not found:
            print(f"Expand column {x}")
            for y in range(len(data)):
                data[y] = data[y][:x] + '.' + data[y][x:]
        x -= 1
            
    return data

def find_galaxies(data):
    g = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "#":
                g.append([y,x])
    return g

def compute_distance(s, d):
    # Distance from start to dest
    dist = abs(s[0] - d[0])
    dist += abs(s[1] - d[1])
    return dist

def expand_galaxies(gals):
    r = [57,69,76,93,96,109,118]
    c = [6, 50, 59, 67, 119]
    # TODO
    new_g = []
    for g in gals:
        rc = sum(i < g[0] for i in r)
        cc = sum(i < g[1] for i in c)
        new_g.append([g[0] + 1000000 * rc - rc, g[1] + 1000000 * cc - cc])
        print(f"Convert {g[0]},{g[1]} to {[g[0] + 1000000 * rc, g[1] + 1000000 * cc]}")
    
    return new_g
    

data = load_file()
data = expand_galaxy(data)
#print(data)
galaxies = find_galaxies(data)
#print(galaxies)

# FIRST
start = 0
dest = 0
ng = len(galaxies)
total = 0
for start in range(0,ng-1):
    for dest in range(start+1,ng):
        dist = compute_distance(galaxies[start], galaxies[dest])
        #print(f"Distance from {start} to {dest} = {dist}")
        total += dist

print(f"FIRST Total = {total}")
# 9432361 too low
# 9605127 - RIGHT

# SECOND
data = load_file()
#print(data)
galaxies = find_galaxies(data)
#print(galaxies)
galaxies = expand_galaxies(galaxies)

start = 0
dest = 0
ng = len(galaxies)
total = 0
for start in range(0,ng-1):
    for dest in range(start+1,ng):
        dist = compute_distance(galaxies[start], galaxies[dest])
        #print(f"Distance from {start} to {dest} = {dist}")
        total += dist

print(f"SECOND Total = {total}")
# 300511146944 (too low)
# 458192146944 (too high)
# 458191688761 RIGHT
