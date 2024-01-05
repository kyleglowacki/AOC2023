# BOILER PLATE
def load_file():
    name = "day19_2023.txt"
    with open(name, "r") as f:
        data = f.read()
        data = data.splitlines()

    return data

def write_to_file(i, lines):
    name = f"day19_2023_{i}.txt"
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




##
##  DAY SPECIFIC
##

def parse_work(line):
    #print(line)
    k,rest = line.split("{")
    # Trim {}
    rest = rest[:-1]
    work = rest.split(",")
    conds = []
    for item in work:
        # Look for :
        if ":" not in item:
            # If no colon, then unconditional jump
            conds.append(["True", item])
            
        else:
            # else statement and true location
            statement, location = item.split(":")
            conds.append([statement, location])
        
    return k, conds
    
    
    return ""
def parse_rating(line):
    # remove {}
    l = line[1:-1]
    rs = l.split(",")
    
    return rs

def parse(data):
    process_ratings = False
    workflows = {}
    ratings = []
    for line in data:
        #print(f"LL = {len(line)}")
        if line == "":
            process_ratings = True
        else:
            if not process_ratings:
                k, conds = parse_work(line)
                workflows[k] = conds
            else:
                ratings.append(parse_rating(line))
    return workflows, ratings

data = load_file()
workflows, ratings = parse(data)

# FIRST
total = 0
for part in ratings:
    x = 0
    m = 0
    a = 0
    s = 0
    for qual in part:
        exec(qual)

    print(f"XMAS = {x} {m} {a} {s}")
    next = "in"
    accepted = False
    
    # Loop over workflows
    done = False
    idx = 0
    while not done:
        conds = workflows[next]
        print(f"Consider flow {conds} at {idx}")
        cond = conds[idx]
        #print(f"Eval {cond[0]}")
        if eval(cond[0]):
            idx = 0
            next = cond[1]
            if next in "AR":
                done = True
        else:
            idx += 1
        #print(f"Cond => {cond} lead to [{next}]")

    if next == "A":
        # if accepted total += rating
        total += (x + m + a + s)
        print(f"Accepted {x+m+a+s} .. {total}")
    else:
        print("Rejected")


print(f"FIRST Total = {total}")
# 489392 


# SECOND

