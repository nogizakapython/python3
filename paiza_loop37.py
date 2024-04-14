num = int(input())
ans = ""
for i in range(1,num+1):
    if i == num:
        ans = ans + str(i)
    else:
        ans = ans + str(i) + " "
print(ans)
