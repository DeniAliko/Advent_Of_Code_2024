import useful
data = useful.openFile(25)

def transpose(list):
    out = []
    for i in range(len(list[0])):
        cache = ""
        for thing in list:
            cache += thing[i]
        out.append(cache)

    return out

locks = []
keys = []
orgData = []
cache = []
for line in data:
    if len(line) > 1:
        cache.append(line)
    else:
        orgData.append(cache)
        cache = []
orgData.append(cache)
for obj in orgData:
    if "#" in obj[0]:
        locks.append(transpose(obj))
    else:
        keys.append(transpose(obj))

lockNum = []
keyNum = []
for lock in locks:
    cache = []
    for row in lock:
        cache.append(row.count("#"))
    lockNum.append(cache)

for key in keys:
    cache = []
    for row in key:
        cache.append(row.count("#"))
    keyNum.append(cache) 

# max = 7
total = 0
seen = []
for i in range(0, len(lockNum)):
    for j in range(0, len(keyNum)):
        focLock = lockNum[i]
        focKey = keyNum[j]
        good = True
        for k in range(len(focLock)):
            if focLock[k] + focKey[k] > 7:
                good = False
                break
        if good:
            total += 1

print(total)