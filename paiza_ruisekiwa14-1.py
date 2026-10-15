str_s = input()
b = [0] * 10
s = [0] * 11

for i in range(10):
    if str_s[i] == "b":
        b[i] = 1

for i in range(10):
    s[i + 1] = s[i] + b[i]

print(s[8] - s[2])