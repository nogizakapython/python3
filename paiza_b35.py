s = input()
t = input()
leng1 = len(t)
leng2 = len(s)
count = 0
for i in range(leng1-leng2+1):
    p = t[i : i + leng2]
    if p == s:
        count += 1
print(count)
