import useful
from queue import Queue
data = useful.openFile(16)
grid = useful.createGrid(data)

for key in grid.keys():
    if grid[key] == "S":
        start = key
    if grid[key] == "E":
        end = key

# new new idea: she dijk on my stra till i pathfinding algorithm

def getNeighbors(node):
    """return [straight, left, right]"""
    x = node[0][0]
    y = node[0][1]
    dir = node[1]

    straight = None
    right = None
    left = None
    if grid[(x+1,y)] != "#":
        if dir == "D":
            straight = ((x+1, y), "D")
        elif dir == "R":
            right = ((x+1, y), "D")
        elif dir == "L":
            left = ((x+1, y), "D")
    if grid[(x-1,y)] != "#":
        if dir == "U":
            straight = ((x-1, y), "U")
        elif dir == "R":
            left = ((x-1, y), "U")
        elif dir == "L":
            right = ((x-1, y), "U")
    if grid[(x,y+1)] != "#":
        if dir == "R":
            straight = ((x, y+1), "R")
        elif dir == "U":
            right = ((x, y+1), "R")
        elif dir == "D":
            left = ((x, y+1), "R")
    if grid[(x,y-1)] != "#":
        if dir == "L":
            straight = ((x, y-1), "L")
        elif dir == "D":
            right = ((x, y-1), "L")
        elif dir == "U":
            left = ((x, y-1), "L")

    return [straight, left, right]

precedents = {}
values = {}
unvisited = []
for key in grid.keys():
    if grid[key] != "#":
        unvisited.append((key, "U"))
        unvisited.append((key, "D"))
        unvisited.append((key, "L"))
        unvisited.append((key, "R"))
        values[(key, "U")] = 100000000000000 if grid[key] != "S" else 0
        values[(key, "D")] = 100000000000000 if grid[key] != "S" else 0
        values[(key, "L")] = 100000000000000 if grid[key] != "S" else 0
        values[(key, "R")] = 100000000000000 if grid[key] != "S" else 0

gate = True
count = 0
while gate:
    gate = False
    if len(unvisited) == 0:
        gate = False
    
    current = None
    currentValue = 100000000000000
    for thingy in unvisited:
        if values[thingy] < 100000000000000:
            gate = True
            if values[thingy] < currentValue:
                currentValue = values[thingy]
                current = thingy
                

    if current != None:
        s, l, r = getNeighbors(current)

        if s != None:
            newVal = currentValue + 1
            if newVal == values[s]:
                precedents[s].append(current)
            if newVal < values[s]:
                precedents[s] = [current]
                values[s] = newVal

        if l != None:
            newVal = currentValue + 1001
            if newVal == values[l]:
                precedents[l].append(current)
            if newVal < values[l]:
                precedents[l] = [current]
                values[l] = newVal

        if r != None:
            newVal = currentValue + 1001
            if newVal == values[r]:
                precedents[r].append(current)
            if newVal < values[r]:
                precedents[r] = [current]
                values[r] = newVal

        unvisited.remove(current)
    
    count += 1
    if count%50 == 0:
        print(count)


dirToCheck = "R" #should be R for real input
print(values[(end, dirToCheck)])

# part 2
q = Queue()
visited = []
q.put((end, dirToCheck))
while not q.empty():
    focus = q.get()
    if focus not in visited:
        visited.append(focus)
        if focus[0] != start:
            for sdf in precedents[focus]:
                q.put(sdf)

visitedCoords = []
for node in visited:
    if node[0] not in visitedCoords:
        visitedCoords.append(node[0])

print(len(visitedCoords))