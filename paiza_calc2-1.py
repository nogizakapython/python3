s = input()

s += "."
add = True
ans = 0
t = ""
for ele in s:
    if ele.isdigit():
        t += ele
    else:
        if add:
            ans += int(t)
        else:
            ans -= int(t)

        if ele == "+":
            add = True
        else:
            add = False

        t = ""

print(ans)
