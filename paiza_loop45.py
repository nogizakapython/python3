num = int(input())
ans = ""
for i in range(1,num+1):
    for j in range(1,i+1):
        if j == i:
            ans = ans + str(j)
        else:
            ans = ans + str(j) + " "
    print(ans)
    ans = ""
