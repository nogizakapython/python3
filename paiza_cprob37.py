a,b = map(str,input().split(' '))
str1 = input()
leng_a = len(str1)
ans_a = 0
ans_b = 0
count = 0
for i in range(0,leng_a):
    c = str1[i]
    if c == "<":
        count += 1
        if count == 1:
            ans_a = i + 1
        elif count == 2:
            ans_b = i + 1

print(str(ans_a) + " " + str(ans_b))
