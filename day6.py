import useful
data = useful.openFile(6)

grid = useful.createGrid(data)

visited = []
for coords in grid.keys():
    if grid[coords] == "^":
        currentPos = [coords[0], coords[1]]
        startPos = [coords[0], coords[1]]
        grid[coords] = "."
        break

bumped = False
direction = "N"
while not bumped:
    if direction == "N":
        if currentPos[0] == 0:
            bumped = True
            break
        else:
            if grid[(currentPos[0]-1, currentPos[1])] == "#":
                direction = "E"
                continue
            currentPos[0] -= 1

    if direction == "E":
        if currentPos[1] == len(data[0])-1:
            bumped = True
            break
        else:
            if grid[(currentPos[0], currentPos[1]+1)] == "#":
                direction = "S"
                continue
            currentPos[1] += 1

    if direction == "S":
        if currentPos[0] == len(data)-1:
            bumped = True
            break
        else:
            if grid[(currentPos[0]+1, currentPos[1])] == "#":
                direction = "W"
                continue
            currentPos[0] += 1

    if direction == "W":
        if currentPos[1] == 0:
            bumped = True
            break
        else:
            if grid[(currentPos[0], currentPos[1]-1)] == "#":
                direction = "N"
                continue
            currentPos[1] -= 1
            
    thingy = [currentPos[0], currentPos[1]]
    visited.append(thingy)

result = []
for coord in visited:
    if coord not in result:
        result.append(coord)
count = 0
print(len(result))