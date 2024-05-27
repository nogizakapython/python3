data = input()
array1 = list(data)
ans = 0
num = len(array1)
sign = ""
for i in range(num):
    if i % 2 == 0:
        number1 = int(array1[i])
        if i == 0:
            ans += number1
        else:
            if sign == "+":
                ans += number1
            elif sign == "-":
                ans -= number1
    else:
        sign = array1[i]

print(ans)
