p = []
ans_p = 0
ans_num = 0

for i in range(4):
    w_array1 = input().split()
    for j in w_array1:
        p.append(j)
    print(p)
for i in range(10):
    if p[i] == "1":
        ans_num += 1
        ans_p = 10 - i

print(ans_p)
print(ans_num)
