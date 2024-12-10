import useful
data = useful.openFile(10)

import queue

grid = useful.createGrid(data)
for key in grid.keys():
    grid[key] = int(grid[key])

def getNeighbors(tuple):
    x = tuple[0]
    y = tuple[1]
    neighbors = []
    if x < len(data)-1 and (grid[(x+1,y)] == grid[(x,y)] + 1):
        neighbors.append((x+1, y))
    if x > 0 and (grid[(x-1,y)] == grid[(x,y)] + 1):
        neighbors.append((x-1, y))
    if y < len(data[0])-1 and (grid[(x,y+1)] == grid[(x,y)] + 1):
        neighbors.append((x, y+1))
    if y > 0 and (grid[(x,y-1)] == grid[(x,y)] + 1):
        neighbors.append((x, y-1)) 

    return neighbors

pos0 = []
for key in grid.keys():
    if grid[key] == 0:
        pos0.append(key)

score = 0
for startingPos in pos0:
    queueue = queue.Queue()
    queueue.put(startingPos)
    visited = []
    thisScore = 0
    while not queueue.empty():
        focus = queueue.get()
        if focus not in visited:
            visited.append(focus)
            if grid[focus] == 9:
                thisScore += 1
            else:
                for neighbor in getNeighbors(focus):
                    queueue.put(neighbor)
    score += thisScore

print(score)

# part 2:
score = 0
for startingPos in pos0:
    queueue = queue.Queue()
    queueue.put(startingPos)
    thisScore = 0
    while not queueue.empty():
        focus = queueue.get()
        if grid[focus] == 9:
            thisScore += 1
        else:
            for neighbor in getNeighbors(focus):
                queueue.put(neighbor)
    score += thisScore
print(score)