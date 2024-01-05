
def load_file():
    name = "day12_2023.txt"
    with open(name, "r") as f:
        data = f.read()
        data = data.splitlines()

    return data

def is_valid(p, s):
    # Check if string s is a valid example of pattern p
    if len(p) != len(s):
        print(f"Pattern {p} and {s} are different lengths")
        return False
    for i in range(len(s)):
        if p[i] != "?" and (p[i] != s[i]):
            return False
    return True

def valid_blank_list(d, max):
    if len(d) < 3:
        return False
    for idx in range(len(d)):
        if d[idx] > max:
            return False
    for idx in range(1,len(d)-1):
        if d[idx] < 1:
            return False
    if sum(d) > max:
        return False
    return True

def gen_nums(max):
    n = []
    for i in range(max+1):
        n.append([i])
    return n

def combine(b,n):
    idx = 0
    s = ""
    # TODO loop on idx
    s += b[idx] * "."
    s += n[idx] * "#"
    return s

def gen_blanks(num_slots, num_blanks):
    # if 3 slots and 5 blanks
    b = []
    for n in range(num_slots):
        b.append(gen_nums(num_blanks))
    print(b)
    return b

def process(pat, n):
    print(f"{n} needs {len(n)-1} to {len(n)+1} gaps")
    blanks = len(pat) - (sum(n)+len(n)-1)
    print(f"Need to add {blanks} to get to {len(pat)}")
    gen_blanks(len(n)+1, blanks)

# TODO ???
    
    return 1


data = load_file()
pats = []
nums = []
for line in data:
    patt, numbers = line.split()
    pats.append(patt)
    numbers = numbers.split(',')
    numbers = [int(n) for n in numbers]
    nums.append(numbers)
    #print(f"{patt} and {numbers}")

# FIRST
total = 0
for i,p in enumerate(pats):
    n = nums[i]
    total += process(p,n)
    exit()

print(f"FIRST Total = {total}")


# SECOND

