import aocd

def GetId(game):
    #print(game)
    hs = game.split(":")
    value = int(hs[0][5:])
    #print(value)
    return value

def ComputeScore(cnt):
    if cnt < 1:
        #print(f"Score = {0} from {cnt}")
        return 0
    else:
        #print(f"Score = {2**(cnt-1)} from {cnt}")
        return 2 ** (cnt-1)

def CountMatches(wins, mine):
    cnt = 0
    for win in wins:
        if win in mine:
            cnt += 1
    #print(wins)
    #print(mine)
    #print(cnt)
    return cnt

raw = aocd.get_data(day=4, year=2023)
data = raw.splitlines()

total = 0

print("FIRST STAR")
for card in data:
    parts = card.split(":")[1]
    parts = parts.split("|")
    #print(parts)
    wins = [int(ele) for ele in parts[0].split()]
    mine = [int(ele) for ele in parts[1].split()]
    
    cntM = CountMatches(wins, mine)
    print(cntM)
    score = ComputeScore(cntM)
    
    total += score

print(f"first total = {total}")

total = 0
print("SECOND STAR")

cardCount = [1] * len(data)
b = [0] * len(data) * 200
cardCount = cardCount + b

for card in data:
    id = GetId(card)
    parts = card.split(":")[1]
    parts = parts.split("|")

    wins = [int(ele) for ele in parts[0].split()]
    mine = [int(ele) for ele in parts[1].split()]
    
    cntM = CountMatches(wins, mine)
    print(f"ID-{id} has {cntM} updating range {id} to {id+cntM}")
    for n in range(id, id+cntM):
        cardCount[n] += cardCount[id-1]

    
print(cardCount[:len(data)])
total = sum(cardCount[:len(data)])
print(f"second total = {total}")
# 55566 too low
