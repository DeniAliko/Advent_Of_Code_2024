import useful
import itertools
data = useful.openFile(7)

equations = []
for line in data:
    cacheline = []
    cachecache = line.split(" ")

    cacheline.append(int(cachecache[0][:-1]))
    cacheline.append([int(cachecache[i]) for i in range(1, len(cachecache))])
    
    equations.append(cacheline)

def getPermutations(n):
    return list(itertools.product([0, 1], repeat=n))

final = 0
for equation in equations:
    targetVal = equation[0]
    good = False
    for order in getPermutations(len(equation[1])-1):
        currentRes = equation[1][0]
        for i in range(len(equation[1])-1):
            if order[i] == 0:
                currentRes += equation[1][i+1]
            if order[i] == 1:
                currentRes *= equation[1][i+1]
        if currentRes == targetVal:
            good = True
            break

    if good:
        final += targetVal

print(final)

def getPermutations(n):
    return list(itertools.product([0, 1, 2], repeat=n))

final2 = 0
for equation in equations:
    targetVal = equation[0]
    good = False
    for order in getPermutations(len(equation[1])-1):
        currentRes = equation[1][0]
        for i in range(len(equation[1])-1):
            if order[i] == 0:
                currentRes += equation[1][i+1]
            if order[i] == 1:
                currentRes *= equation[1][i+1]
            if order[i] == 2:
                currentRes = int(str(currentRes) + str(equation[1][i+1]))
        if currentRes == targetVal:
            good = True
            break

    if good:
        final2 += targetVal

print(final2)