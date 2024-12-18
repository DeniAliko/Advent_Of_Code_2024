import useful
data1 = useful.openFile(18)
from queue import Queue

size = 70
initDrop = 1024
grid = {}
for i in range(0, size + 1):
    for j in range(0, size + 1):
        grid[(i,j)] = "."

data = [(int(line.split(",")[1]), int(line.split(",")[0]))for line in data1]

for i in range(initDrop):
    grid[data[i]] = "#"

start = (0,0)
end = (size, size)

score = 0

def getNeighbors(tuple):
    x = tuple[0]
    y = tuple[1]
    neighbors = []
    if x < size and (grid[(x+1,y)] == "."):
        neighbors.append((x+1, y))
    if x > 0 and (grid[(x-1,y)] == "."):
        neighbors.append((x-1, y))
    if y < size and (grid[(x,y+1)] == "."):
        neighbors.append((x, y+1))
    if y > 0 and (grid[(x,y-1)] == "."):
        neighbors.append((x, y-1)) 

    return neighbors

vis = []
for i in range(0, size + 1):
    cacheStr = ""
    for j in range(0, size + 1):
        cacheStr += grid[(i,j)]

    vis.append(cacheStr)

# useful.printList(vis)


values = {}
unvisited = []
for key in grid.keys():
    if grid[key] != "#":
        unvisited.append(key)
        values[key] = 100000000000000 if key != (0,0) else 0

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
        neighbors = getNeighbors(current)

        for neighbor in neighbors:
            newVal = currentValue + 1
            if newVal < values[neighbor]:
                values[neighbor] = newVal

        unvisited.remove(current)


print(values[(size, size)])
# part 2
# what if I jsut do it 71649287364981 times
for i in range(initDrop, len(data)):
    grid[data[i]] = "#"

    values = {}
    unvisited = []
    for key in grid.keys():
        if grid[key] != "#":
            unvisited.append(key)
            values[key] = 100000000000000 if key != (0,0) else 0

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
            neighbors = getNeighbors(current)

            for neighbor in neighbors:
                newVal = currentValue + 1
                if newVal < values[neighbor]:
                    values[neighbor] = newVal

            unvisited.remove(current)
        
        count += 1
        if count%500 == 0:
            print(count)

    print(str(i) + "--------------------")
    if values[(size, size)] == 100000000000000:
        print(str(data[i][1]) + "," + str(data[i][0]))
        break