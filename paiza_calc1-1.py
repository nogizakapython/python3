s = input()
t = input()

ans = ""
for i in range(len(s)):
    ans += str(int(s[i]) + int(t[i]))

print(ans)
