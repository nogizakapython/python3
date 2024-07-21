p = []
ans_p = 0
ans_num = 0

for i in range(4):
    p += input().split()
    print(p)
for i in range(10):
    if p[i] == "1":
        ans_num += 1
        ans_p = 10 - i

print(ans_p)
print(ans_num)
