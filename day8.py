import useful
data = useful.openFile(8)

grid = useful.createGrid(data)

possibles = set()
for coords in grid:
    if grid[coords] != ".":
        possibles.add(grid[coords])

antinodes = []
xmax = len(data)
ymax = len(data[0])

for frequency in possibles:
    locs1 = []
    for coords in grid:
        if grid[coords] == frequency:
            locs1.append(coords)
    locs = []
    for thing in locs1:
        if thing not in locs:
            locs.append(thing)

    for i in range(len(locs)):
        for j in range(len(locs)):
            if i != j:
                midpoint = [(locs[i][0] + locs[j][0])*0.5, (locs[i][1] + locs[j][1])*0.5]
                di = [midpoint[0]-locs[i][0], midpoint[1]-locs[i][1]]
                dj = [midpoint[0]-locs[j][0], midpoint[1]-locs[j][1]]
                antinode1 = [midpoint[0] + (-3)*(di[0]), midpoint[1] + (-3)*(di[1])]
                antinode2 = [midpoint[0] + (-3)*(dj[0]), midpoint[1] + (-3)*(dj[1])]

                antinodes.append(antinode1)
                antinodes.append(antinode2)

result = []
for thing in antinodes:
    if thing not in result:
        if thing[0] >= 0 and thing[0] < xmax and thing[1] >= 0 and thing[1] < ymax:
            result.append([int(thing[0]), int(thing[1])])

# print(result)
print(len(result))

# part 2:
antinodes = []

for frequency in possibles:
    locs1 = []
    for coords in grid:
        if grid[coords] == frequency:
            locs1.append(coords)
    locs = []
    for thing in locs1:
        if thing not in locs:
            locs.append(thing)

    for i in range(len(locs)):
        for j in range(len(locs)):
            if i != j:
                for k in range(0, 100):
                    midpoint = [(locs[i][0] + locs[j][0])*0.5, (locs[i][1] + locs[j][1])*0.5]
                    di = [midpoint[0]-locs[i][0], midpoint[1]-locs[i][1]]
                    dj = [midpoint[0]-locs[j][0], midpoint[1]-locs[j][1]]
                    antinode1 = [midpoint[0] + (-(k))*(di[0]), midpoint[1] + (-(k))*(di[1])]
                    antinode2 = [midpoint[0] + (-(k))*(dj[0]), midpoint[1] + (-(k))*(dj[1])]

                    antinodes.append(antinode1)
                    antinodes.append(antinode2)

result = []
for thing in antinodes:
    if thing not in result:
        if thing[0] % 1 == 0 and thing[1] % 1 == 0:
            if thing[0] >= 0 and thing[0] < xmax and thing[1] >= 0 and thing[1] < ymax:
                result.append([int(thing[0]), int(thing[1])])

# print(result)
print(len(result))