import useful
data = useful.openFile(11)
import queue

data = [int(i) for i in data[0].split(" ")]
current = data[:]

# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

for l in range(25):
    q = queue.Queue()
    new = []
    for i in range(len(current)):
        q.put(current[i])
    while not q.empty():
        focus = q.get()
        if focus == 0:
            new.append(1)
        elif len(str(focus)) % 2 == 0:
            firstHalf = int(str(focus)[:int(len(str(focus))/2)])
            secondHalf = int(str(focus)[int(len(str(focus))/2):])
            new.append(firstHalf)
            new.append(secondHalf)
        else:
            new.append(focus * 2024)
    current = new[:]
print(len(current))
# lmao brute force

freqDict = {}
for i in data:
    freqDict[i] = data.count(i)

for l in range(75):
    newDict = {}
    for e in freqDict.keys():
        newDict[e] = 0
    for e in freqDict.keys():
        if e == 0:
            if 1 not in newDict.keys():
                newDict[1] = freqDict[0]
            else:
                newDict[1] += freqDict[0]
        elif len(str(e)) % 2 == 0:
            firstHalf = int(str(e)[:int(len(str(e))/2)])
            secondHalf = int(str(e)[int(len(str(e))/2):])
            if firstHalf not in newDict.keys():
                newDict[firstHalf] = freqDict[e]
            else:
                newDict[firstHalf] += freqDict[e]
            if secondHalf not in newDict.keys():
                newDict[secondHalf] = freqDict[e]
            else:
                newDict[secondHalf] += freqDict[e]        
        else:
            if e*2024 not in newDict.keys():
                newDict[e*2024] = freqDict[e]
            else:
                newDict[e*2024] += freqDict[e]

    freqDict = newDict.copy()

final = 0
for key in freqDict.keys():
    final += freqDict[key]

print(final)