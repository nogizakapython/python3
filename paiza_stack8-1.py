# 自分の得意な言語で
# Let's チャレンジ！！
n,x = map(int,input().split())
max_sum = 0
array1 = list(map(int,input().split()))
t_sum = 0
ans_array = []
l = 0
flag = False
while flag == False:
    if x >= 1:
        for j in range(0,x):
            t_sum += array1[j]
    if t_sum > max_sum:
        if l > 0:
            ans_array.pop(0)
        ans_array.append(array1[0])
        max_sum = t_sum
    array1.pop(0)
    t_sum = 0
    l = len(array1)
    if x > l:
        flag = True
    

print(str(max_sum) + " " + str(ans_array[0]))