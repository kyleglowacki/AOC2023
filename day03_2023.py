import aocd

def GetNumber(data, row, col):
    val = ""
    val += data[row][col]
    idx = col
    while True:
        idx += 1
        if idx >= len(data[0]):
            # Stop looking if we get to the end of the row
            break
        else:
            if data[row][idx].isdigit():
                val += data[row][idx]
            else:
                # Stop looking if we don't find a numeric digit
                break
    #print(f"Val is {val}")
    return int(val)

def IsNewNumber(data, row, col):
    if col == 0:
        return data[row][col].isdigit()
    else:
        return data[row][col].isdigit() and not data[row][col-1].isdigit()


def IsPartNumber(data, row, col, num):
    # Search around the number for symbols
    # how big is the number? row, col is leftmost digit
    startCol = max(col-1,0)
    endCol = col
    while data[row][endCol].isdigit():
        endCol += 1
        # Make sure we don't go off the board
        if endCol >= len(data[0]):
            endCol = len(data[0])-1
            break
        #print(f"About to Check {row},{endCol}")
    
    startRow = max(row-1, 0)
    endRow = min(row+1, len(data[0])-1)

    #print(f"Searching from {startRow},{startCol} to {endRow},{endCol}")

    for r in range(startRow, endRow+1):
        for c in range(startCol, endCol+1):
            if not (data[r][c].isdigit() or (data[r][c] == '.')):
                # Anything else is a symbol
                #print(f"Found {data[r][c]} near {num}")
                return True
    
    return False

def UpdateGear(gears, r, c, n):
    for g in gears:
        #print(f"{g}  {r}  {c}  {n}")
        if (g[0] == r) and (g[1] == c):
            g[2].append(n)
            return gears
    print("UNEXPECTED")

def IsGear(data, row, col, num):
    # input row, col are first digit in num on the data grid
    startCol = max(col-1,0)
    endCol = col
    while data[row][endCol].isdigit():
        endCol += 1
        # Make sure we don't go off the board
        if endCol >= len(data[0]):
            endCol = len(data[0])-1
            break
        #print(f"About to Check {row},{endCol}")
    
    startRow = max(row-1, 0)
    endRow = min(row+1, len(data[0])-1)

    #print(f"Searching from {startRow},{startCol} to {endRow},{endCol}")

    for r in range(startRow, endRow+1):
        for c in range(startCol, endCol+1):
            if data[r][c] == "*":
                # Anything else is a symbol
                #print(f"Found {data[r][c]} near {num}")
                return True, r, c
    
    return False, 0, 0
    
raw = aocd.get_data(day=3, year=2023)
data = raw.splitlines()
#print(data)

rows = len(data)
cols = len(data[0])
print(f"Board Size rows={rows} and cols={cols}")
total = 0

print("FIRST STAR")
for row in range(rows):
    for col in range(cols):
        if IsNewNumber(data, row, col):
            num = GetNumber(data, row, col)
            if IsPartNumber(data, row, col, num):
                #print(f"Found part number {num}")
                total += num

print(f"first total = {total}")

total = 0
print("SECOND STAR")
gears = []

for row in range(rows):
    for col in range(cols):
        if data[row][col] == "*":
            gears.append([row, col, []])

#print(gears)
            
for row in range(rows):
    for col in range(cols):
        if IsNewNumber(data, row, col):
            num = GetNumber(data, row, col)
            isG, r, c = IsGear(data, row, col, num)
            if isG:
                gears = UpdateGear(gears, r, c, num)
                
for g in gears:
    if len(g[2]) == 2:
        val = g[2][0] * g[2][1]
        #print(f"Gear Value = {g[2][0]}*{g[2][1]} = {val}")
        total += val
                
print(f"second total = {total}")
