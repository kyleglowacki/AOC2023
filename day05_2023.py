def LoadMap(data, idx):
    toMap = []
    #print(f"Index - {idx}")
    while "map" not in data[idx]:
        v = data[idx]
        #print(f"Looking at {v}")
        if len(v) > 2:
            values = [int(s) for s in v.split()]
            toMap.append(values)
        # ELSE "blank line"
        idx += 1
        if idx == len(data):
            break
    #print(f"Return {idx}")
    return toMap, idx+1


def LoadFile():
    name = "day05_2023.txt"
    with open(name, "r") as f:
        data = f.read()
        data = data.splitlines()

        
    seeds = data[0].split(":")[1]
    seeds = [int(s) for s in seeds.split()]

    idx = 3
    toSoil, idx = LoadMap(data, idx)
    toFert, idx = LoadMap(data, idx)
    toWater, idx = LoadMap(data, idx)
    toLight, idx = LoadMap(data, idx)
    toTemp, idx = LoadMap(data, idx)
    toHumid, idx = LoadMap(data, idx)
    toLocation, idx = LoadMap(data, idx)
    
    return seeds, toSoil, toFert, toWater, toLight, toTemp, toHumid, toLocation

SRC_START = 1
DEST_START = 0
RANGE = 2

def Lookup(mappings, value):
    for m in mappings:
        if (value >= m[SRC_START]) and (value < m[SRC_START] + m[RANGE]):
            #print(f"Mapped {value} using {m}")
            #print(f"  Answer is {m[DEST_START] + (value - m[SRC_START])} = {m[DEST_START]} + ({value} - {m[SRC_START]})")
            return m[DEST_START] + (value - m[SRC_START])
    return value


def Divideup(mappings, pair):
    rngs = []
    # Idea is to take(inclusive) [[1,10]] and convert it to [[1,3],[40,43],[8,10]] based on mapping of [40, 4, 4]
    print(f"DIVIDEUP TOP {len(pair)}")
    for m in mappings:
        # mappings
        map_start = m[SRC_START]
        map_end = m[SRC_START] + m[RANGE]
        dest_start = m[DEST_START]
        #print(f"Map {m} ... {map_start} to {map_end}")
        idx = 0
        while idx < len(pair):
            # Check if the start/stop in this pair are covered in any of the mappings
            #print(f"PAIR {pair[idx]}")

            # ranges
            seed_start = pair[idx][0]
            seed_end = pair[idx][1]
            
            # Already entirely inside mapped region.  DONE
            if (map_start <= seed_start <= map_end) and (map_start <= seed_end <= map_end):
                print(f"PAIR = {pair}   seed window entirely inside mapped region")
                pass

            # First Digit in, last digit out
            elif (map_start <= seed_start <= map_end) and not (map_start <= seed_end <= map_end):
                # Find where it leaves and divide into two ranges
                pair.append([seed_start, map_end])
                pair.append([map_end+1, seed_end])
                pair.pop(idx)
                print(f"PAIR = {pair}  seed start in mapped window; seed end overflows end")
                break

            # First Digit in, last digit out
            elif (not(map_start <= seed_start <= map_end)) and (map_start <= seed_end <= map_end):
                pair.append([seed_start, map_start-1])
                pair.append([map_start, seed_end])
                pair.pop(idx)
                print(f"PAIR = {pair}  seed end in mapped window; seed start is prior to window start")
                break
            # If our seed range contains the whole mapped zone
            elif (seed_start < map_start) and (map_end < seed_end):
                pair.append([seed_start, map_start-1])
                pair.append([map_start, map_end])
                pair.append([map_end+1, seed_end])
                pair.pop(idx)
                print(f"PAIR = {pair}  seed window encapsulated entire mapped region")
                break

            print(f"PAIR = {pair}  No overlap at all")
            idx += 1

    # Now . do the mapping
    for m in mappings:
        # mappings
        map_start = m[SRC_START]
        map_end = m[SRC_START] + m[RANGE]
        dest_start = m[DEST_START]
        idx = 0
        while idx < len(pair):                     
            #print(f"PAIR {pair[idx]}")

            # ranges
            seed_start = pair[idx][0]
            seed_end = pair[idx][1]

            # Do we have ANYTHING to do with this pair/mapping?
            if (map_start <= seed_start <= map_end) and (map_start <= seed_end <= map_end):
                rngs.append([dest_start + (seed_start-map_start), dest_start + (seed_end-map_start)])
                print(f"Map {m} ... {map_start} to {map_end} ... move to {dest_start}")
                print(f"[{seed_start},{seed_end}] becomes [{dest_start + (seed_start-map_start)}, {dest_start + (seed_end-map_start)}]")
            idx += 1

    return rngs

seeds, toSoil, toFert, toWater, toLight, toTemp, toHumid, toLocation = LoadFile()
#print(seeds)
ans = []

for seed in seeds:
    a = Lookup(toSoil, seed)
    b = Lookup(toFert, a)
    c = Lookup(toWater, b)
    d = Lookup(toLight, c)
    e = Lookup(toTemp, d)
    f = Lookup(toHumid, e)
    g = Lookup(toLocation, f)
    #print(f"Map {seed} to {a} to {b} to {c} to {d} to {e} to {f} to {g}")

    ans.append(g)

print(f"Answers = {ans}")
print(f"Smallest = {min(ans)}")


# SECOND
ans = []
it = iter(seeds)
sp = zip(it,it)
#for p in sp:
#    print(p)
g = []
for p in sp:
    pp = [p[0], p[0] + p[1]]
    print(f"Starting {pp}")
    a = Divideup(toSoil, [ pp ])
    b = Divideup(toFert, a)
    c = Divideup(toWater, b)
    d = Divideup(toLight, c)
    e = Divideup(toTemp, d)
    f = Divideup(toHumid, e)
    g = Divideup(toLocation, f)
    print(f"Map {p} to {a} to {b} to {c} to {d} to {e} to {f} to {g}")

    # List of pairs in g.. iterate and find min
    value = 999999999999
    for p in g:
        print(f"Checking {p} in {g} ... current {value}")
        value = min(value, p[0])
    ans.append(value)

print(f"Answers = {ans}")
print(f"P2 Smallest = {min(ans)}")
# 11611182 RIGHT!
# 28497630 too high
# 2998499327 too high
# 3009990758 (also too high .. didn't even try)
