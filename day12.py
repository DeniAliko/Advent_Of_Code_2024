import useful
data = useful.openFile(12)
from queue import Queue

grid = useful.createGrid(data)

def getNeighbors(tuple, dir = False):
    x = tuple[0]
    y = tuple[1]
    neighbors = []
    if x < len(data)-1 and (grid[(x+1,y)] == grid[(x,y)]):
        neighbors.append((x+1, y))
    if x > 0 and (grid[(x-1,y)] == grid[(x,y)]):
        neighbors.append((x-1, y))
    if y < len(data[0])-1 and (grid[(x,y+1)] == grid[(x,y)]):
        neighbors.append((x, y+1))
    if y > 0 and (grid[(x,y-1)] == grid[(x,y)]):
        neighbors.append((x, y-1))

    return neighbors

found = []
unfound = [key for key in grid.keys()]
regions = []

def getRegion(tuple):
    q = Queue()
    q.put(tuple)

    visited = []
    while not q.empty():
        focus = q.get()
        if focus not in visited:
            visited.append(focus)
            for neighbor in getNeighbors(focus):
                q.put(neighbor)
    
    # print("found region", len(found), "/", len(data)*len(data[0]))
    return visited

while len(found) != len(data)*len(data[0]):
    focus = unfound[0]
    
    a = getRegion(focus)
    regions.append(a)
    for thing in a:
        found.append(thing)
        unfound.remove(thing)

score = 0
for region in regions:
    a = len(region)
    p = len(region) * 4
    for coord in region:
        p -= len(getNeighbors(coord))

    score += a * p

print(score)
# part 2:

def getNeighborsDiag(tuple):
    x = tuple[0]
    y = tuple[1]
    neighbors = []
    dneighbors = []
    if x < len(data)-1 and (grid[(x+1,y)] == grid[(x,y)]):
        neighbors.append((x+1, y))
    if x > 0 and (grid[(x-1,y)] == grid[(x,y)]):
        neighbors.append((x-1, y))
    if y < len(data[0])-1 and (grid[(x,y+1)] == grid[(x,y)]):
        neighbors.append((x, y+1))
    if y > 0 and (grid[(x,y-1)] == grid[(x,y)]):
        neighbors.append((x, y-1))

    if x < len(data)-1 and y < len(data[0])-1 and (grid[(x+1,y+1)] == grid[(x,y)]):
        dneighbors.append((x+1, y+1))
    if x > 0 and y < len(data[0])-1 and (grid[(x-1,y+1)] == grid[(x,y)]):
        dneighbors.append((x-1, y+1))
    if x > 0 and y < y > 0 and (grid[(x-1,y-1)] == grid[(x,y)]):
        dneighbors.append((x-1, y-1))
    if x < len(data)-1 and y > 0 and (grid[(x+1,y-1)] == grid[(x,y)]):
        dneighbors.append((x+1, y-1))

    return [neighbors, dneighbors]

score = 0
for region in regions:
    corners = 0
    for coord in region:
        x = coord[0]
        y = coord[1]
        neighbors = getNeighbors(coord)
        if (x-1, y) not in region:
            if (x-1, y+1) in region:
                corners += 1
            elif (x, y+1) not in region:
                corners += 1

        if (x+1, y) not in region:
            if (x+1, y-1) in region:
                corners += 1
            elif (x, y-1) not in region:
                corners += 1

        if (x, y+1) not in region:
            if (x+1, y+1) in region:
                corners += 1
            elif (x+1, y) not in region:
                corners += 1
        
        if (x, y-1) not in region:
            if (x-1, y-1) in region:
                corners += 1
            elif (x-1, y) not in region:
                corners += 1

    score += corners * len(region)

print(score)
