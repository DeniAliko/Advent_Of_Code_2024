import useful

data = useful.openFile(4)

lines = []
for line in data:
    lines.append(line)
    lines.append(line[::-1])

for i in range(len(data[0])):
    cacheLine = ""
    for line in data:
        cacheLine += line[i]

    lines.append(cacheLine)
    lines.append(cacheLine[::-1])

for i in range(len(data)):
    cacheLine = ""
    for j in range(i+1):
        cacheLine += data[i-j][j]
    lines.append(cacheLine)
    lines.append(cacheLine[::-1])

dataPrime = []
for i in range(len(data)-1, -1, -1):
    dataPrime.append(data[i][::-1])
for i in range(len(dataPrime)-1):
    cacheLine = ""
    for j in range(i+1):
        cacheLine += dataPrime[i-j][j]
    lines.append(cacheLine)
    lines.append(cacheLine[::-1])

dataPrime = []
for i in range(len(data)-1, -1, -1):
    dataPrime.append(data[i])
for i in range(len(dataPrime)):
    cacheLine = ""
    for j in range(i+1):
        cacheLine += dataPrime[i-j][j]
    lines.append(cacheLine)
    lines.append(cacheLine[::-1])

dataPrime = []
for i in range(len(data)):
    dataPrime.append(data[i][::-1])
for i in range(len(dataPrime)-1):
    cacheLine = ""
    for j in range(i+1):
        cacheLine += dataPrime[i-j][j]
    lines.append(cacheLine)
    lines.append(cacheLine[::-1])

total = 0
for line in lines:
    total += line.count("XMAS")
print(total)

# pt 2:
total = 0
for x in range(1, len(data)-1):
    for y in range(1, len(data)-1):
        if data[x][y] == "A":
            if data[x-1][y-1] == "M" and data[x-1][y+1] == "M" and data[x+1][y-1] == "S" and data[x+1][y+1] == "S":
                total += 1
                continue
            elif data[x-1][y-1] == "S" and data[x-1][y+1] == "S" and data[x+1][y-1] == "M" and data[x+1][y+1] == "M":
                total += 1
                continue
            elif data[x-1][y-1] == "M" and data[x-1][y+1] == "S" and data[x+1][y-1] == "M" and data[x+1][y+1] == "S":
                total += 1
                continue
            elif data[x-1][y-1] == "S" and data[x-1][y+1] == "M" and data[x+1][y-1] == "S" and data[x+1][y+1] == "M":
                total += 1
                continue

print(total)