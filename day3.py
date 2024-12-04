import useful
data = useful.openFile(3)
total = 0

for i in range(len(data)):
    split1 = data[i].split("mul")
    # print(split1)
    split2 = []
    for line in split1:
        if line[0] == "(":
            split2.append(line[1:])
    # print(split2)
    split3 = []
    for line in split2:
        split3.append(line.split(")")[0])
    # print(split3)
    for line in split3:
        if len(line.split(",")) != 1:
            if (line.split(",")[0] + line.split(",")[1]).isdigit():
                total += int(line.split(",")[0]) * int(line.split(",")[1])

print(total)

# pt 2:
total = 0
for i in range(len(data)):
    split0 = data[i].split("do()")
    split1 = []
    for line in split0:
        split1.append(line.split("don't()")[0])
    # print(split1)
    split1point5 = []
    for line in split1:
        for subline in line.split("mul"):
            split1point5.append(subline)
    split2 = []
    for line in split1point5:
        if len(line) != 0:
            if line[0] == "(":
                split2.append(line[1:])
    # print(split2)
    split3 = []
    for line in split2:
        split3.append(line.split(")")[0])
    # print(split3)
    for line in split3:
        if len(line.split(",")) != 1:
            if (line.split(",")[0] + line.split(",")[1]).isdigit():
                total += int(line.split(",")[0]) * int(line.split(",")[1])
print(total)