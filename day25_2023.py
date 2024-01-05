import networkx as nx

# BOILER PLATE
def load_file():
    name = "day25_2023.txt"
    with open(name, "r") as f:
        data = f.read()
        data = data.splitlines()

    return data

def write_to_file(i, lines):
    name = f"day25_2023_{i}.txt"
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

def add_one_way_map(maps, first, second):
    try:
        #print(f"{maps} {first} {second}")
        orig = maps[first]
        orig.append(second)
        maps[first] = orig
    except KeyError:
        maps[first] = [second]
    return maps

def add_two_way_map(maps, first, second):
    maps = add_one_way_map(maps, first, second)
    maps = add_one_way_map(maps, second, first)
    return maps
    
def parse_line(maps, l, graph):
    first, rest = l.split(":")
    pieces = rest.split()
    for piece in pieces:
        print(f"Add mapping {first} <==> {piece}")
        maps = add_two_way_map(maps, first, piece)
        graph.add_edge(first, piece)
    return maps

# REAL DATA (571547834 combinations (select 3 from 1509))
data = load_file()
# SAMPLE DATA (455 combinations (select 3 from 15))
data2 = ["jqt: rhn xhk nvd",
         "rsh: frs pzl lsr",
         "xhk: hfx",
         "cmg: qnr nvd lhk bvb",
         "rhn: xhk bvb hfx",
         "bvb: xhk hfx",
         "pzl: lsr hfx nvd",
         "qnr: nvd",
         "ntq: jqt hfx bvb xhk",
         "nvd: lhk",
         "lsr: lhk",
         "rzs: qnr cmg lsr rsh",
         "frs: qnr lhk lsr"]

# FIRST STAR
maps = {}
graf = nx.Graph()
for line in data:
    maps = parse_line(maps, line, graf)

num_cut, parts = nx.stoer_wagner(graf)
print(f"Number of cuts = {num_cut}")
print(f"Len 1 {len(parts[0])}")
print(f"Len 2 {len(parts[1])}")
print(f"ANS = {len(parts[0]) * len(parts[1])}")


# SECOND STAR
total = 0
# no second star..
