import aocd
import math

def computeScores(time):
    values = []
    for t in range(time):
        values.append(t * (time-t))
    return values

# Try to go faster, the calculation is based on two values multiplied and
# peaking when they are equal.. so provide the sqrt of the threshold
# as the starting point of the search
def computeBinaryScores(time, thres):
    values = []
    mid = int(math.sqrt(thres))
    frontDone = False
    backDone = False

    idx = mid
    while (not frontDone):
        if idx < 1:
            frontDone = True
        val = idx * (time - idx)
        if val > thres:
            values.append(val)
        else:
            print("Found front at {idx}")
            frontDone = True
        idx -= 1

    idx = mid+1
    while (not backDone):
        if idx == time:
            backDone = True
        val = idx * (time - idx)
        if val > thres:
            values.append(val)
        else:
            print("Found back at {idx}")
            backDone = True
        idx += 1
    
    return values
        
def winners(values, threshold):
    wins = []
    for v in values:
        if v > threshold:
            wins.append(v)
    return wins
        
raw = aocd.get_data(day=6, year=2023)
data = raw.splitlines()

#data = ['Time:      7  15   30','Distance:  9  40  200']

time = data[0].split()[1:]
time = [int(i) for i in time]
print(time)

dist = data[1].split()[1:]
dist = [int(i) for i in dist]
print(dist)

total = 1
print("FIRST STAR")
idx = 0
for idx in range(len(time)):

    v = computeScores(time[idx])
    w = winners(v, dist[idx])
    count = len(w)
    #print(f"SCORES = {v}")
    #print(len(v))
    #print(f"WINS = {w}")
    #print(len(w))
    #print(count)
    total *= count

print(f"first total = {total}")


time = data[0].split(':')[1:]
time = time[0].replace(' ','')
time = int(time)
print(time)

dist = data[1].split(':')[1:]
dist = dist[0].replace(' ','')
dist = int(dist)
print(dist)
total = 0
print("SECOND STAR")
v = computeBinaryScores(time, dist)
w = winners(v, dist)
total = len(w)
print(f"second total = {total}")
