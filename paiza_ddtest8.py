# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
calc = input()
enzan = calc[1]
A = int(calc[0])
B = int(calc[2])
ans = 0
if enzan == "+":
    ans = A + B 
elif enzan == "-":
    ans = A - B 
elif enzan == "x":
    ans = A * B
print(ans)