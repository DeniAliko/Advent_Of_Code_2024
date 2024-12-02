import useful

data = useful.openFile(2)
lists = [[int(j) for j in i.split()] for i in data]

count = 0
for i in range(len(lists)):
    focus = lists[i]
    parityCheck = False
    gapsCheck = True
    for j in range(len(focus)-1):
        if abs(focus[j]-focus[j+1]) not in [1, 2, 3]:
            gapsCheck = False

    increasing = False
    decreasing = False
    equalExists = False
    for j in range(len(focus)-1):
        if focus[j] < focus[j+1]:
            increasing = True
        elif focus[j] > focus[j+1]:
            decreasing = True
        elif focus[j] == focus[j+1]:
            equalExists = True
    
    if (equalExists == False) and (increasing != decreasing):
        parityCheck = True

    if parityCheck and gapsCheck:
        count += 1

print(count)



count = 0
for i in range(len(lists)):
    focus = lists[i]
    subSafeCount = 0
    for k in range(len(focus)):
        newFocus = focus[:k] + focus[k+1:]
        parityCheck = False
        gapsCheck = True
        for j in range(len(newFocus)-1):
            if abs(newFocus[j]-newFocus[j+1]) not in [1, 2, 3]:
                gapsCheck = False

        increasing = False
        decreasing = False
        equalExists = False
        for j in range(len(newFocus)-1):
            if newFocus[j] < newFocus[j+1]:
                increasing = True
            elif newFocus[j] > newFocus[j+1]:
                decreasing = True
            elif newFocus[j] == newFocus[j+1]:
                equalExists = True
        
        if (equalExists == False) and (increasing != decreasing):
            parityCheck = True

        if parityCheck and gapsCheck:
            subSafeCount += 1

    if subSafeCount > 0:
        count += 1

print(count)