import useful
data = useful.openFile(21)
import itertools

numpad = ["789", "456", "123", " 0A"]
numpad = useful.createGrid(numpad)
keypad = [" ^A", "<v>"]
keypad = useful.createGrid(keypad)


def evalKey(str):
    chars = [char for char in str]
    result = ""
    pos = list(find(keypad, "A"))
    for char in chars:
        if char == "A":
            result += keypad[(pos[0], pos[1])]
        if char == "<":
            pos[1] -= 1
        if char == ">":
            pos[1] += 1
        if char == "^":
            pos[0] -= 1
        if char == "v":
            pos[0] += 1

    return result

def find(dict, target):
    for i in dict.keys():
        if dict[i] == target:
            return i

def getPermutations(n):
    return list(itertools.product([False, True], repeat=n))

def numToKey(str, swap = False):
    des = [char for char in str]
    pos = list(find(numpad, "A"))
    res = ""
    for dest in des:
        destCoord = list(find(numpad, dest))
        delta = [destCoord[0]-pos[0], destCoord[1]-pos[1]]
        if numpad[(pos[0], pos[1])] in ["0", "A"]:
            if delta[0] > 0:
                res = res + ("v" * delta[0])
            if delta[0] < 0:
                res = res + ("^" * abs(delta[0]))
            if delta[1] > 0:
                res = res + (">" * delta[1])
            if delta[1] < 0:
                res = res + ("<" * abs(delta[1]))
        elif swap:
            if delta[0] > 0:
                res = res + ("v" * delta[0])
            if delta[0] < 0:
                res = res + ("^" * abs(delta[0]))
            if delta[1] > 0:
                res = res + (">" * delta[1])
            if delta[1] < 0:
                res = res + ("<" * abs(delta[1]))
        else:
            if delta[1] > 0:
                res = res + (">" * delta[1])
            if delta[1] < 0:
                res = res + ("<" * abs(delta[1]))
            if delta[0] > 0:
                res = res + ("v" * delta[0])
            if delta[0] < 0:
                res = res + ("^" * abs(delta[0]))
            
        
        res += "A"
        pos = destCoord[:]

    return res

def keyToKey(str, swap = False):
    des = [char for char in str]
    pos = list(find(keypad, "A"))
    res = ""
    for dest in des:
        destCoord = list(find(keypad, dest))
        delta = [destCoord[0]-pos[0], destCoord[1]-pos[1]]
        if keypad[(pos[0], pos[1])] in ["<"]:
            if delta[0] > 0:
                res = res + ("v" * delta[0])
            if delta[0] < 0:
                res = res + ("^" * abs(delta[0]))
            if delta[1] > 0:
                res = res + (">" * delta[1])
            if delta[1] < 0:
                res = res + ("<" * abs(delta[1]))
        elif swap:
            if delta[0] > 0:
                res = res + ("v" * delta[0])
            if delta[0] < 0:
                res = res + ("^" * abs(delta[0]))
            if delta[1] > 0:
                res = res + (">" * delta[1])
            if delta[1] < 0:
                res = res + ("<" * abs(delta[1]))
        else:
            if delta[1] > 0:
                res = res + (">" * delta[1])
            if delta[1] < 0:
                res = res + ("<" * abs(delta[1]))
            if delta[0] > 0:
                res = res + ("v" * delta[0])
            if delta[0] < 0:
                res = res + ("^" * abs(delta[0]))
        
        res += "A"
        pos = destCoord[:]

    return res

def getPart1(str):
    vals = []
    listOfPerms = getPermutations(3)
    for perm in listOfPerms:
        vals.append(len(keyToKey(keyToKey(numToKey(str, perm[0]), perm[1]), perm[2])))
    return min(vals)

total = 0
for i in data:
    total += getPart1(i) * int(i[:-1])
    print(getPart1(i), int(i[:-1]))
print(total)
# 213458 too high
# 219558 too high
# 215546 no way

# useful.printList(["789", "456", "123", " 0A"])
# print("---------")
# useful.printList([" ^A", "<v>"])