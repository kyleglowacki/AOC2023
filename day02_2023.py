import aocd

def GetId(game):
    print(game)
    hs = game.split(":")
    value = int(hs[0][5:])
    #print(value)
    return value

def IsPossible(game):
    rounds = game.split(":")[1].split(";")
    for round in rounds:
        pairs = round.split(",")
        for p in pairs:
            red = 0
            green = 0
            blue = 0
            v = p.split()
            #print(v)
            if v[1] == 'red':
                red = int(v[0])
            if v[1] == 'green':
                green = int(v[0])
            if v[1] == 'blue':
                blue = int(v[0])
            if ((red > 12) or (green > 13) or (blue > 14)):
                return False
                
    return True

def PowerOf(game):
    rounds = game.split(":")[1].split(";")
    red = 0
    green = 0
    blue = 0
    for round in rounds:
        pairs = round.split(",")
        for p in pairs:
            v = p.split()
            #print(v)
            if v[1] == 'red':
                red = max(red, int(v[0]))
            if v[1] == 'green':
                green = max(green, int(v[0]))
            if v[1] == 'blue':
                blue = max(blue, int(v[0]))
    print(f"{red} {green}  {blue} = {red*green*blue}")
    return red * green * blue


raw = aocd.get_data(day=2, year=2023)
data = raw.splitlines()

total = 0

print("FIRST STAR")
for game in data:
    id = GetId(game)

    possible = IsPossible(game)
    
    if possible:
        total += id

print(f"first total = {total}")

total = 0
print("SECOND STAR")
for game in data:
    id = GetId(game)

    v = PowerOf(game)
    total += v

print(f"second total = {total}")
