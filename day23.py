import useful
from queue import Queue
data = useful.openFile(23)

connections = {}
couples1 = [i.split("-") for i in data]
couples = []
for i in couples1:
    couples.append(i)
    couples.append(i[::-1])
computers = []
for i in couples:
    if i[0] not in computers:
        computers.append(i[0])

for i in computers:
    for j in couples:
        if j[0] == i:
            if i not in connections:
                connections[i] = [j[1]]
            else:
                connections[i].append(j[1])


# print(connections)
cycles = []
for start in computers:
    if start[0] == "t":
        step1 = connections[start]
        step2 = [(i, connections[i]) for i in step1]
        # print(step2)

        trios = []

        for thing in step2:
            for a in thing[1]:
                if start in connections[a]:
                    trios.append([start, thing[0], a])

        # print(trios)
        for j in [sorted(i) for i in trios]:
            if j not in cycles:
                cycles.append(j)
# print(cycles)
print(len(cycles))

# party = 0
max = []
r = []
p = computers[:]
x = []
def bk(R, P, X):
    if len(P) == 0 and len(X) == 0:
        max.append(R)

    else:
        for x in P:
            pIntN = []
            xIntN = []
            for i in connections[x]:
                if i in P:
                    pIntN.append(i)
                if i in X:
                    xIntN.append(i)
            bk(R + [x], pIntN, xIntN)
            P.remove(x)
            X.append(x)

bk(r, p, x)

theMax = []
for i in max:
    if len(i) > len(theMax):
        theMax = i
theMax = sorted(theMax)
out = ""
for i in theMax:
    out += i
    out += ","

out = out[:-1]
print(out)