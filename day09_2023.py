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

def extrapolate_vals(vals):
    idx = len(vals)-1
    vals[idx].append(0)
    print(f"Adding 0 to row {idx}")
    while idx > 0:
        idx -= 1
        # New value for row idx is
        # last element of row idx + 
        # Last element of row idx+1
        new_val = last_element(vals[idx]) + last_element(vals[idx+1])
        print(f"Adding {new_val} to row {idx}")
        vals[idx].append(new_val)
        #import pdb;pdb.set_trace()
    return vals

def extrapolate_backwards_vals(vals):
    idx = len(vals)-1
    vals[idx].insert(0,0)
    print(f"Adding 0 to front of row {idx}")
    while idx > 0:
        idx -= 1
        # New value for row idx is
        # first element of row idx - 
        # first element of row idx+1
        new_val = first_element(vals[idx]) - first_element(vals[idx+1])
        print(f"Adding {new_val} to row {idx}")
        vals[idx].insert(0,new_val)
        #import pdb;pdb.set_trace()
    return vals



raw = aocd.get_data(day=9, year=2023)
data = raw.splitlines()
#print(data)

total = 0
total2 = 0
print("******************* FIRST STAR ***************")
for line in data:
    vals = []
    t = line.split()
    for i,v in enumerate(t):
        t[i] = int(v)
    vals.append(t)
    vals = fill_to_zero(vals)
    vals = extrapolate_vals(vals)
    total += vals[0][len(vals[0])-1]
    vals = extrapolate_backwards_vals(vals)
    total2 += vals[0][0]
    
    #print(vals)
    #exit()
print(f"FIRST total = {total}")

print("********** SECOND STAR *************")
print(f"SECOND total = {total2}")
