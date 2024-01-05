import aocd
import numpy

def check(l, v):
    return l and [v]*len(l) == l

def fill_to_zero(vals):

    idx = 0
    while not check(vals[len(vals)-1], 0):
        #print(vals[idx])
        vals.append(list(numpy.diff(vals[idx])))
        idx += 1

    return vals

def last_element(a):
    return a[len(a)-1]

def first_element(a):
    return a[0]

def findIntersection(x1,y1,x2,y2,x3,y3,x4,y4):
    px= ( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) ) 
    py= ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
    return [px, py]

def comp_intersection(first, second):
    a = first
    a2 = [a[0]+a[3], a[1]+a[4], a[2]+a[5], a[3],a[4],a[5]]
    b = second
    b2 = [b[0]+b[3], b[1]+b[4], b[2]+b[5], b[3],b[4],b[5]]
    ans = findIntersection(a[0],a[1],a2[0],a2[1],b[0],b[1],b2[0],b2[1])
    return ans

def parse_line(line):
    parts = line.split("@")
    x,y,z = parts[0].split(',')
    xv,yv,zv = parts[1].split(',')
    
    return [int(x), int(y), int(z), int(xv), int(yv), int(zv)]

def past(val, ans):
    x = val[0]
    y = val[1]
    xdot = val[3]
    ydot = val[4]
    if (ans[0] > x) and (xdot < 0):
        # X has to increase but xdot is negative
        return True
    if (ans[1] > y) and (ydot < 0):
        # Y has to increase but ydot is negative
        return True
    if (ans[0] < x) and (xdot > 0):
        # X has to decrease but xdot is positive
        return True
    if (ans[1] < y) and (ydot > 0):
        # X has to increase but xdot is negative
        return True

    return False

raw = aocd.get_data(day=24, year=2023)
data = raw.splitlines()
data2 = ["19, 13, 30 @ -2,  1, -2",
        "18, 19, 22 @ -1, -1, -2",
        "20, 25, 34 @ -2, -2, -4",
        "12, 31, 28 @ -1, -2, -1",
        "20, 19, 15 @  1, -5, -3"]
#minxy = 7
#maxxy = 27 
minxy = 200000000000000
maxxy = 400000000000000

vals = []
for line in data:
    vals.append(parse_line(line))
#print(data)

total = 0
total2 = 0
cnt = 0
print("******************* FIRST STAR ***************")
for idx, val in enumerate(vals):
    for idx2 in range(idx+1, len(vals)):
        try:
            cnt += 1
            print("================================================")
            print(f"Pairing {cnt}")
            print(f"Hailstone A : {vals[idx]}")
            print(f"Hailstone B : {vals[idx2]}")
            ans = comp_intersection(vals[idx], vals[idx2])
            print(f"Intersection : {ans}")
            if (ans[0] >= minxy) and (ans[0] <= maxxy) and (ans[1] >= minxy) and (ans[1] <= maxxy):

                if past(vals[idx], ans):
                    print("RESULT -  Intersect in the past for A")                    
                elif past(vals[idx2], ans):
                    print("RESULT -  Intersect in the past for B")
                else:
                    total += 1 
                    print("RESULT -  Intersect in range")
            else:
                print("RESULT - Intersect NOT in range")
        except ZeroDivisionError:
            print("RESULT - Intersect : None - Parallel")
            

# TODO 20512 is too high
print(f"FIRST total intersections in test area = {total}")

print("********** SECOND STAR *************")
print(f"SECOND total = {total2}")
