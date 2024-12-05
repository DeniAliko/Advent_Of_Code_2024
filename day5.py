import useful
data = useful.openFile(5)
data1 = useful.openFile("5a")

rules = []
for line in data:
    rules.append([int(i) for i in line.split("|")])

updates = []
for line in data1:
    updates.append([int(i) for i in line.split(",")])

sum = 0
bads = []
for line in updates:
    good = True
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            if [line[j], line[i]] in rules:
                good = False
    if good:
        sum += line[int(len(line)/2)]
    else:
        bads.append(line)

print(sum)
# holy shit top 1000 globally

# part 2:
# def orderIsPossible(line):
#     if len(line) == 1:
#         return True
#     for rule in rules:
#         if rule[0] == line[0] and rule[1] in line:
#             if orderIsPossible(line[1:]):
#                 print(line[0])
#                 return True

nowGoods = []
for line in bads:
    potentialOrder = []
    actualOrder = []
    for i in range(len(line)):
        ruleQueue = []
        for rule in rules:
            if rule[0] == line[i] and rule[1] in line:
                ruleQueue.append(rule)
        
        potentialOrder.append([line[i], len(ruleQueue)])
    for j in range(len(potentialOrder)):
        for thingy in potentialOrder:
            if thingy[1] == j:
                actualOrder.append(thingy[0])
    nowGoods.append(actualOrder[::-1])
    
total = 0
for line in nowGoods:
    total += line[int(len(line)/2)]
print(total)