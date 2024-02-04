# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
array1 = input_line.split(' ')
A = int(array1[0])
B = int(array1[1])
C = int(array1[2])
D = int(array1[3])
E = 0
F = 0
G = 0
if A == 1 or B == 1:
    E = 1
else:
    E = 0

if E == 1 and C == 1:
    F = 1
else:
    F = 0

if F == 1 and D == 1:
    G = 0
elif F == 0 and D == 0:
    G = 0
else:
    G = 1


print(G)
