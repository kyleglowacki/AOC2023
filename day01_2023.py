import aocd

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def getFirst(word):
    for letter in word:
        if letter.isnumeric():
            return int(letter)


def indexOfFirst(word):
    n = len(numbers)
    index = [999999] * n
    for number in range(n):
        try:
            index[number] = word.index(numbers[number])
        except ValueError:
            pass
    return min(index),index.index(min(index))+1

def indexOfLast(word):
    n = len(numbers)
    index = [-1] * n
    for number in range(n):
        try:
            index[number] = word.rindex(numbers[number])
        except ValueError:
            pass
    return max(index),index.index(max(index))+1

def getFirstNumber(word):

    idxIntoWord,number = indexOfFirst(word)
    #print(f"Found {number} at {idxIntoWord}")
    
    for i in range(idxIntoWord):
        if word[i].isnumeric():
            return int(word[i])

    return number
            
                        
        
def getLastNumber(word):
    l = len(word)

    idxIntoWord,number = indexOfLast(word)
    #print(f"Found {number} at {idxIntoWord}")
    
    for i in reversed(range(idxIntoWord, l)):
        if word[i].isnumeric():
            return int(word[i])

    return number
            
                        
        
raw = aocd.get_data(day=1, year=2023)

data = raw.splitlines()
# ['sq5fivetwothree1','six5gc' .. ]

#data = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']

total = 0

print("FIRST STAR")
for word in data:
    first = getFirst(word) * 10
    last = getFirst(reversed(word))
    sum = last + first
    total += sum

print(f"first total = {total}")

total = 0
print("SECOND STAR")
for word in data:
    first = getFirstNumber(word) * 10
    last = getLastNumber(word)
    #print(f"{word} \n Found {first} and {last}\n\n")
    sum = last + first
    total += sum

print(f"second total = {total}")
