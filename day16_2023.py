# BOILER PLATE
def load_file():
    name = "day16_2023.txt"
    with open(name, "r") as f:
        data = f.read()
        data = data.splitlines()

    return data

def write_to_file(i, lines):
    name = f"day16_2023_{i}.txt"
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

##
##  DAY SPECIFIC
##

def generate_beams(data, nb, beam, d, e):
    max_row = len(data[0])
    max_col = len(data)
    nr = beam[0] + d[beam[2]][0]
    nc = beam[1] + d[beam[2]][1]
    #print(f"Move beam from [{beam[0]}, {beam[1]}] to [{nr}, {nc}], moving {beam[2]}")
    
    if (nr < 0) or (nc < 0) or (nr >= max_row) or (nc >= max_col):
        # left the data
        print("Drop beam... left the board")
    else:
        e[nr][nc] = 1
        if ((beam[2] == "E") or (beam[2] == "W")):
            if (data[nr][nc] == "|"):
                nb.append([nr,nc,"N"])
                nb.append([nr,nc,"S"])
            elif (data[nr][nc] == "\\"):
                if beam[2] == "E":
                    nb.append([nr,nc,"S"])
                else:                            
                    nb.append([nr,nc,"N"])
            elif (data[nr][nc] == "/"):
                if beam[2] == "E":
                    nb.append([nr,nc,"N"])
                else:                            
                    nb.append([nr,nc,"S"])
            elif (data[nr][nc] == ".") or (data[nr][nc] == "-"):
                nb.append([nr,nc,beam[2]])
            else:
                print(f"Unknown EW character - {data[nr][nc]}")
        elif ((beam[2] == "N") or (beam[2] == "S")):
            if (data[nr][nc] == "-"):
                nb.append([nr,nc,"E"])
                nb.append([nr,nc,"W"])
            elif (data[nr][nc] == "\\"):
                if beam[2] == "N":
                    nb.append([nr,nc,"W"])
                else:                            
                    nb.append([nr,nc,"E"])
            elif (data[nr][nc] == "/"):
                if beam[2] == "N":
                    nb.append([nr,nc,"E"])
                else:                            
                    nb.append([nr,nc,"W"])
            elif (data[nr][nc] == ".") or (data[nr][nc] == "|"):
                nb.append([nr,nc,beam[2]])
            else:
                print(f"Unknown NS character - {data[nr][nc]}")
    #print(f"New Beams - {nb}")
    return nb, e

def process(data, d, b, e):

    # beam databse
    bdb = {}
    steps = 0
    done = False
    while not done:
        nb = []

        if len(b) == 0:
            print("No beams.. AT TOP")
        
        # move beams
        # update e
        # update beams
        nb = []
        for beam in b:
            kv = str(beam[0]) + "," + str(beam[1]) + "," + beam[2]
            added, bdb = add_to_db(bdb, kv)
            if added:
                nb, e = generate_beams(data, nb, beam, d, e)
            else:
                print(f"Beam is duplicate/cycle .. {beam}")
        b = nb
        steps += 1
        #print(f"Step {steps}, beams = {len(b)}")

        ## BEAMS form loops.. how to detect?
        if len(b) == 0:
            #print("No beams.. done")
            done = True

    return e


data = load_file()
d = {"E":[0,1],"W":[0,-1],"N":[-1,0],"S":[1,0]}
# SAMPLE DATA
data2 = [".|...\....",
        "|.-.\.....",
        ".....|-...",
        "........|.",
        "..........",
        ".........\\",
        "..../.\\\..",
        ".-.-/..|..",
        ".|....-|.\\",
        "..//.|...."]

# FIRST STAR
# 6622

# SECOND STAR
total = 0
# From the West
for x in range(len(data)):
    energized = make_grid(len(data), len(data[0]), 0)
    start_position = [x, -1, "E"]
    beams = []
    beams, energized = generate_beams(data, beams, start_position, d, energized)
    energized = process(data, d, beams, energized)
    value = cnt_data(energized, 1)
    print(f"Value of {start_position} is {value}")
    total = max(total, value)
print(f"                                Best of the West = {total}")

# From the East
for x in range(len(data)):
    energized = make_grid(len(data), len(data[0]), 0)
    start_position = [x, len(data[x]), "W"]
    beams = []
    beams, energized = generate_beams(data, beams, start_position, d, energized)
    energized = process(data, d, beams, energized)
    value = cnt_data(energized, 1)
    print(f"Value of {start_position} is {value}")
    total = max(total, value)
print(f"                                Best after the East = {total}")

# From the South
for x in range(len(data[0])):
    energized = make_grid(len(data), len(data[0]), 0)
    start_position = [len(data), x, "N"]
    beams = []
    beams, energized = generate_beams(data, beams, start_position, d, energized)
    energized = process(data, d, beams, energized)
    value = cnt_data(energized, 1)
    print(f"Value of {start_position} is {value}")
    total = max(total, value)
print(f"                                Best after the South = {total}")

# From the North
for x in range(len(data[0])):
    energized = make_grid(len(data), len(data[0]), 0)
    start_position = [-1, x, "S"]
    beams = []
    beams, energized = generate_beams(data, beams, start_position, d, energized)
    energized = process(data, d, beams, energized)
    value = cnt_data(energized, 1)
    print(f"Value of {start_position} is {value}")
    total = max(total, value)
print(f"                                Best after the North = {total}")

