# 自分の得意な言語で
# Let's チャレンジ！！
n,x = map(int,input().split())
max_sum = 0
array1 = list(map(int,input().split()))
ans_array = []
for i in range(n-x+1):
    t_sum = 0
    for j in range(x):
        t_sum += array1[i + j]
    if t_sum > max_sum:
        max_sum = t_sum
        ans_array.append(array1[i])

ans = len(ans_array)
print(str(max_sum) + " " + str(ans_array[ans - 1]))