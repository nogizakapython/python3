num = int(input())
ans = ""
for i in range(1,10):
    cal = num * i
    if i == 9:
        ans = ans + str(cal)
    else:
        ans = ans + str(cal) + " "
print(ans)
