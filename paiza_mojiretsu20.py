s = input()

if "." not in s:
    i = 0
    while i < len(s):
        if s[i] != "0":
            break
        i += 1

    if i == len(s):
        print(0)
    else:
        print(s[i:])
else:
    ans = ""
    start = 0

    for i in range(len(s)):
        if s[i] != "0":
            if s[i] == ".":
                ans += "0"

            start = i
            break

    last = 0
    for i in range(len(s)):
        if s[i] != "0":
            last = i

    first_dot = s.find(".")
    for i in range(start, last + 1):
        if s[i] != ".":
            ans += s[i]
        elif i == first_dot:
            ans += s[i]

    print(ans)
