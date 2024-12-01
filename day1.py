import useful

data = useful.openFile(1)

list1 = []
list2 = []
for i in range(len(data)):
    # print(data[i].split(" "))
    list1.append(int(data[i].split(" ")[0]))
    list2.append(int(data[i].split(" ")[3]))

list1.sort()
list2.sort()

sum = 0
for i in range(len(list1)):
    sum += abs(list1[i]-list2[i])
# pt 1
print(sum)
sum = 0
for i in range(len(list1)):
    sum += (list1[i] * list2.count(list1[i]))
print(sum)