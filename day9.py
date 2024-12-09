import useful
data1 = useful.openFile(9)
from itertools import groupby

data = []
for i in range(len(data1[0])):
    data.append(int(data1[0][i]))

formattedLine = []
count = 0
fileNum = 0
maxNum = 0
for i in range(len(data)):
    if i%2 == 0:
        # for j in range(data[i])
        [formattedLine.append(count) for j in range(data[i])]
        count += 1
        maxNum += 1
        fileNum += data[i]
    elif i%2 == 1:
        [formattedLine.append(".") for j in range(data[i])]


result = []
pickIndex = len(formattedLine)-1
for i in range(len(formattedLine)):
    if formattedLine[i] != ".":
        result.append(formattedLine[i])
    else:
        while formattedLine[pickIndex] == ".":
            pickIndex -= 1
        result.append(formattedLine[pickIndex])
        pickIndex -= 1

final = 0
for i in range(fileNum):
    final += i * result[i]
print(final)
# ---------------------------------------------------------------------
org = []
count = 0
for i in range(len(data)):
    if i % 2 == 0:
        if data[i] != 0:
            org.append([count, data[i]])
            count += 1
    else:
        if data[i] != 0:
            org.append([".", data[i]])

asdf = [thing for thing in org]

def move(current, numToLookFor):
    current.reverse()
    index = 0
    for i in range(len(current)):
        if current[i][0] == numToLookFor:
            index = i
            break

    focus = current[index][:]
    current[index] = [".", focus[1]]
    for i in range(len(current)-1, -1, -1):
        if current[i][0] == "." and current[i][1] >= focus[1]:
            current = current[:i] + [[".", current[i][1] - focus[1]]] + [focus] + current[i+1:]
            break
    
    out = []
    for thing in current:
        if thing[1] != 0:
            out.append(thing)
    out.reverse()
    if out[-1][0] == ".":
        out.pop(-1)
    return out

for i in range(maxNum):
    asdf = move(asdf, maxNum - i)
    # if i%5 == 0:
    #     print("moved", i, "/", maxNum)
result = []
for thing in asdf:
    for k in range(thing[1]):
        result.append(str(thing[0]))

final = 0
for i in range(len(result)):
    if result[i] != ".":
        final += i * int(result[i])
print(final)