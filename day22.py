import useful
data = useful.openFile(22)

def secret(num, iterations):
    a = num
    path = [a]
    for i in range(iterations):
        a = a ^ a * 64
        a = a % 16777216

        a = a ^ int((a/32))
        a = a % 16777216

        a = a ^ a * 2048
        a = a % 16777216

        path.append(a)

    return (a, path)

secretNumLists = {}
count = 0
for i in range(len(data)):
    g = secret(int(data[i]), 2000)
    count += g[0]
    secretNumLists[int(data[i])] = g[1]
    print(i, len(data))

print(count)
# part 2
maps = {}
count = 0
for g in data:
    num = int(g)
    path = secretNumLists[num]
    mapToAdd = {}
    for i in range(4, 2000):
        deltas = ((path[i-3]%10) - (path[i-4]%10), (path[i-2]%10) - (path[i-3]%10), (path[i-1]%10) - (path[i-2]%10), (path[i]%10) - (path[i-1]%10))
        mapToAdd[deltas] = path[i] % 10

    maps[num] = mapToAdd
    count += 1
    print("Map made:", count, len(data))

actualValues = {}
seenDeltas1 = []
for map in maps:
    for i in maps[map].keys():
        seenDeltas1.append(i)

seenDeltas = set(seenDeltas1)

count = 0

for map in maps:
    for delta in maps[map].keys():
        if delta not in actualValues.keys():
            actualValues[delta] = maps[map][delta]
        else:
            actualValues[delta] += maps[map][delta]
    count += 1
    if count%50 == 0:
        print("sum found!", count, len(seenDeltas))

maxDelta = None
maxSum = 0
count = 0
for delta in actualValues:
    if actualValues[delta] >= maxSum:
        maxSum = actualValues[delta]
        maxDelta = delta
        print("New max found!-----------------------------------")
    count += 1
    print(count, len(actualValues))

print(maxDelta)
print(maxSum)
# 2269 too high