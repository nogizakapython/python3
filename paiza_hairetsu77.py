num = int(input())
count = 0
for b in range(1,num):
    for c in range(1,num-b):
        a = num - b - c

        ans1 = pow(a,2)
        ans2 = pow(b,2)
        ans3 = pow(c,2)
        ans4 = ans2 + ans3
        if ans1 == ans4:
            count += 1


if count >= 1:
    print("YES")
else:
    print("NO")
