s = input()
t = int(input())

if t == 0:
    print(0)
else:
    ans = ""
    upper = 0
    for i in range(len(s) - 1, -1, -1):
        z = int(s[i]) * t + upper
        upper = z // 10
        ans = str(z % 10) + ans

        if i == 0 and upper > 0:
            ans = str(upper) + ans

    print(ans)
