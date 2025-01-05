import useful
data = useful.openFile(19)
p = data[0].split(", ")
t = data[2:]

done = {}
def check(towel):
    inDone = False
    if towel in done:
        inDone = True
    if inDone:
        return done[towel]

    if towel == "":
        return True
    
    found = False
    for pattern in p:
        if towel[0:len(pattern)] == pattern:
            if check(towel[len(pattern):]) == True:
                found = True

    if not inDone:
        done[towel] = found
    return found
        
final = 0
for towel in t:
    if check(towel):
        final += 1
    # print(towel, check(towel))

print(final)

# part 2:
done2 = {}
def checkNum(towel):
    memoized = False
    if towel in done2:
        memoized = True
        return done2[towel]
    
    if len(towel) == 0:
        return 1

    num = 0
    for pattern in p:
        if towel[0:len(pattern)] == pattern:
            num += checkNum(towel[len(pattern):])

    if not memoized:
        done2[towel] = num
    return num


final = 0
for towel in t:
    final += checkNum(towel)
    print(towel, checkNum(towel))

print(final)