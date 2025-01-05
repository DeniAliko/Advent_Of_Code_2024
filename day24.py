import useful
data = useful.openFile(24)
split = data.index("SPLIT")
wires = data[:split]
gates = data[split+1:]

wireVals = {}
for i in wires:
    wireVals[i.split(":")[0]] = True if i.split(" ")[1] == "1" else False

ands = {}
ors = {}
xors = {}
equalses = {}
for line in gates:
    spaceSplit = line.split(" ")
    if spaceSplit[1] == "OR":
        if (spaceSplit[0], spaceSplit[2]) in ors.keys():
            equalses[spaceSplit[4]] = ors[(spaceSplit[0], spaceSplit[2])]
        else:
            ors[(spaceSplit[0], spaceSplit[2])] = spaceSplit[4]
        if spaceSplit[0] not in wireVals.keys():
            wireVals[spaceSplit[0]] = None
        if spaceSplit[2] not in wireVals.keys():
            wireVals[spaceSplit[2]] = None
        if spaceSplit[4] not in wireVals.keys():
            wireVals[spaceSplit[4]] = None
    elif spaceSplit[1] == "XOR":
        if (spaceSplit[0], spaceSplit[2]) in xors.keys():
            equalses[spaceSplit[4]] = xors[(spaceSplit[0], spaceSplit[2])]
        else:
            xors[(spaceSplit[0], spaceSplit[2])] = spaceSplit[4]
        if spaceSplit[0] not in wireVals.keys():
            wireVals[spaceSplit[0]] = None
        if spaceSplit[2] not in wireVals.keys():
            wireVals[spaceSplit[2]] = None
        if spaceSplit[4] not in wireVals.keys():
            wireVals[spaceSplit[4]] = None
    elif spaceSplit[1] == "AND":
        if (spaceSplit[0], spaceSplit[2]) in ands.keys():
            equalses[spaceSplit[4]] = ands[(spaceSplit[0], spaceSplit[2])]
        else:
            ands[(spaceSplit[0], spaceSplit[2])] = spaceSplit[4]
        if spaceSplit[0] not in wireVals.keys():
            wireVals[spaceSplit[0]] = None
        if spaceSplit[2] not in wireVals.keys():
            wireVals[spaceSplit[2]] = None
        if spaceSplit[4] not in wireVals.keys():
            wireVals[spaceSplit[4]] = None

def doneCheck():
    out = True
    for i in wireVals.keys():
        if i in equalses.keys():
            wireVals[i] = wireVals[equalses[i]]


    for i in wireVals.keys():
        if wireVals[i] == None:
            out = False
            break
    return out

while True:
    # print("did")
    for wire in wireVals.keys():

        for key in ands.keys():
            if key[0] == wire and wireVals[key[0]] != None:
                if wireVals[key[1]] != None:
                    wireVals[ands[key]] = wireVals[key[0]] and wireVals[key[1]]
            if key[1] == wire and wireVals[key[1]] != None:
                if wireVals[key[0]] != None:
                    wireVals[ands[key]] = wireVals[key[0]] and wireVals[key[1]]

        for key in ors.keys():
            if key[0] == wire and wireVals[key[0]] != None:
                if wireVals[key[1]] != None:
                    wireVals[ors[key]] = wireVals[key[0]] or wireVals[key[1]]
            if key[1] == wire and wireVals[key[1]] != None:
                if wireVals[key[0]] != None:
                    wireVals[ors[key]] = wireVals[key[0]] or wireVals[key[1]]

        for key in xors.keys():
            if key[0] == wire and wireVals[key[0]] != None:
                if wireVals[key[1]] != None:
                    wireVals[xors[key]] = wireVals[key[0]] ^ wireVals[key[1]]
            if key[1] == wire and wireVals[key[1]] != None:
                if wireVals[key[0]] != None:
                    wireVals[xors[key]] = wireVals[key[0]] ^ wireVals[key[1]]
    gate = doneCheck()
    if gate:
        break

zees = []
for i in wireVals:
    if "z" in i:
        if i not in zees:
            zees.append(i)
zees = sorted(zees)
val = []
for i in zees:
    val.append(1 if wireVals[i] else 0)

final = 0
for i in range(len(val)):
    final += val[i] * (2**i)
print(final)