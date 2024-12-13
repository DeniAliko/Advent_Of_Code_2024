import useful
data = useful.openFile(13)
import math

data1 = []
cache = []
for line in data:
    if line != "":
        cache.append(line)
    else:
        data1.append(cache)
        cache = []
data1.append(cache)

machines = []
for cache in data1:
    a = [int(cache[0].split("+")[1].split(",")[0]), int(cache[0].split("+")[2])]
    b = [int(cache[1].split("+")[1].split(",")[0]), int(cache[1].split("+")[2])]
    prize = [int(cache[2].split("=")[1].split(",")[0]), int(cache[2].split("=")[2])]
    machines.append([a,b,prize])

cost = 0
for machine in machines:
    a = machine[0]
    b = machine[1]
    p = machine[2]
    costs = []
    for i in range(1, 101):
        for j in range(1, 101):
            if i*a[0] + j*b[0] == p[0] and i*a[1] + j*b[1] == p[1]:
                costs.append(i*3 + j)

    if len(costs) != 0:
        cost += min(costs)

print(cost)

# part 2:
cost = 0
for machine in machines:
    machine[2][0] += 10000000000000
    machine[2][1] += 10000000000000
    
    a = machine[0]
    b = machine[1]
    p = machine[2]
    det = a[0]*b[1] - a[1]*b[0]
    if det != 0:
        i = (p[0]*b[1]-b[0]*p[1])/det
        j = (p[1]*a[0]-a[1]*p[0])/det
        if i%1 == 0 and j%1 == 0:
            cost += 3*(i) + (j)

print(int(cost))

