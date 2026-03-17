# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

n = int(input())
array1 = list(map(int,input().split(" ")))
l = len(array1)
mem1 = 0.0
tousa_flag = True
for i in range(0,l-1):
    data1 = array1[i]
    data2 = array1[i+1]
    ans = 0.0
    if i == 0:
        mem1 = float(data2 - data1)
    if i > 0:
        ans1 = float(data2 - data1)
        if ans1 != mem1:
            tousa_flag = False
    if tousa_flag == False:
        break

if tousa_flag == True:
    print("Yes")
else:
    print("No")
            

mem2 = 0.0
touhi_flag = True
for i in range(0,l-2):
    data1 = array1[i]
    data2 = array1[i+1]
    data3 = array1[i+2]
    ans = 0.0
    if data1 * data3 != data2 * data2:
        touhi_flag = False
    

if touhi_flag == True:
    print("Yes")
else:
    print("No")        
