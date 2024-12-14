import useful
data = useful.openFile(14)
from queue import Queue

bots = []
for line in data:
    a = line.split("=")
    b = a[1]
    c = a[2]
    v = [int(i) for i in c.split(",")]
    p = [int(i) for i in b.split(" ")[0].split(",")]
    bots.append([p, v])

xmax = 101
ymax = 103

for bot in bots:
    p = bot[0]
    v = bot[1]
    p[0] += v[0] * 100
    p[1] += v[1] * 100

    p[0] = p[0] % xmax
    p[1] = p[1] % ymax

q1 = 0
q2 = 0
q3 = 0
q4 = 0
for bot in bots:
    xmid = (xmax/2) - 0.5
    ymid = (ymax/2) - 0.5
    p = bot[0]
    if p[0] < xmid and p[1] < ymid:
        q1 += 1
    elif p[0] > xmid and p[1] < ymid:
        q2 += 1
    elif p[0] < xmid and p[1] > ymid:
        q3 += 1
    elif p[0] > xmid and p[1] > ymid:
        q4 += 1

print(q1*q2*q3*q4)

# part 2

bots = []
for line in data:
    a = line.split("=")
    b = a[1]
    c = a[2]
    v = [int(i) for i in c.split(",")]
    p = [int(i) for i in b.split(" ")[0].split(",")]
    bots.append([p, v])

grid = [["."] * xmax for i in range(ymax)]
for bot in bots:
    p = bot[0]
    grid[p[1]][p[0]] = "#"

def getNeighbors(coord):
    # [x, y]
    x = coord[0]
    y = coord[1]
    neighbors = []
    if grid[y][x-1] == "#":
        neighbors.append([x-1, y])
    if grid[y][x+1] == "#":
        neighbors.append([x+1, y])
    if grid[y-1][x] == "#":
        neighbors.append([x, y-1])
    if grid[y+1][x] == "#":
        neighbors.append([x, y+1])
    return neighbors

count = 0
while True:
    for bot in bots:
        p = bot[0]
        v = bot[1]
        p[0] += v[0]
        p[1] += v[1]

        p[0] = p[0] % xmax
        p[1] = p[1] % ymax
    
    count += 1
    if count % 100 == 0:
        print(count)
    found = False
    grid = [["."] * xmax for i in range(ymax)]
    for bot in bots:
        p = bot[0]
        grid[p[1]][p[0]] = "#"

    longestStreak = 0
    for line in grid:
        current = 0
        for i in range(len(line)):
            if line[i] == "#":
                current += 1
            elif line[i] == ".":
                if longestStreak < current:
                    longestStreak = current
                current = 0

    if longestStreak >= 12:

        vis = []
        for line in grid:
            cache = ""
            for x in line:
                cache += x

            vis.append(cache)
        useful.printList(vis)
        print("-" * 98, count)
        break

    if count >= 10000:
        print("BAD BREAK")
        break