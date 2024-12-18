import useful

sample = False

global a
global b
global c
a = 51342988 if not sample else 729
b = 0
c = 0
i = [2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0] if not sample else [0,1,5,4,3,0]
p = 0
result = []

def combo(op):
    if op == 4:
        return a
    elif op == 5:
        return b
    elif op == 6:
        return c
    else:
        return op

def adv(op):
    global a
    global b
    global c
    global p
    global result
    global i
    cop = combo(op)
    denom = 2**cop
    a = int(str(a/denom).split(".")[0])
    p += 2

def bxl(op):
    global a
    global b
    global c
    global p
    global result
    global i
    b = b ^ op
    p += 2

def bst(op):
    global a
    global b
    global c
    global p
    global result
    global i
    b = combo(op) % 8
    p += 2

def jnz(op):
    global a
    global b
    global c
    global p
    global result
    global i
    if a != 0:
        p = op
    else:
        p += 2

def bxc(op):
    global a
    global b
    global c
    global p
    global result
    global i
    b = b ^ c
    p += 2

def out(op):
    global a
    global b
    global c
    global p
    global result
    global i
    result.append(combo(op) % 8)
    p += 2

def bdv(op):
    global a
    global b
    global c
    global p
    global result
    global i
    cop = combo(op)
    num = a
    denom = 2**cop
    b = int(str(num/denom).split(".")[0])
    p += 2

def cdv(op):
    global a
    global b
    global c
    global p
    global result
    global i    
    cop = combo(op)
    num = a
    denom = 2**cop
    c = int(str(num/denom).split(".")[0])
    p += 2

while True:
    if i[p] == 0:
        adv(i[p+1])
        if p > len(i) - 2:
            break
    elif i[p] == 1:
        bxl(i[p+1])
        if p > len(i) - 2:
            break
    elif i[p] == 2:
        bst(i[p+1])
        if p > len(i) - 2:
            break
    elif i[p] == 3:
        jnz(i[p+1])
        if p > len(i) - 2:
            break
    elif i[p] == 4:
        bxc(i[p+1])
        if p > len(i) - 2:
            break
    elif i[p] == 5:
        out(i[p+1])
        if p > len(i) - 2:
            break
    elif i[p] == 6:
        bdv(i[p+1])
        if p > len(i) - 2:
            break
    elif i[p] == 7:
        cdv(i[p+1])
        if p > len(i) - 2:
            break

print(result)