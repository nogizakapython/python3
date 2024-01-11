# Let's チャレンジ！！
num = int(input())
array1 = []
array2 = []
max_num = 0
max_man = ""
for i in range(0,num):
    data = input()
    array1.append(data)

set1 = set(array1)
for i in set1:
    name = i
    cnt = array1.count(name)
    array2.append(name + ":" + str(cnt))


for j in list(array2):
    array3 = j.split(":")
    name1 = array3[0]
    cnt1 = int(array3[1])
    if cnt1 > max_num:
        max_man = name1
        max_num = cnt1

print(max_man)

