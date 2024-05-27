s = input()

ans = 0
add = True
for i in range(len(s)):
    if i % 2 == 0:
        if add:
            ans += int(s[i])
        else:
            ans -= int(s[i])
    else:
        if s[i] == "+":
            add = True
        else:
            add = False

print(ans)
