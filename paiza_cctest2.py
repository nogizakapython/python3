# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
A,B,C = input().split(" ")
ans1 = A + B + C 
ans2 = A + C + B 
ans3 = B + A + C 
ans4 = B + C + A
ans5 = C + A + B 
ans6 = C + B + A 
array1 = [ans1,ans2,ans3,ans4,ans5,ans6]
array2 = []

for elem in array1:
    data = int(elem)
    array2.append(data)
    
print(max(array2))