# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

number_array = []
name_array = []



def getnum(number):
    return number_array[number]
    
def getname(number):
    return name_array[number]
    
    
n = int(input())

for i in range(n):
    work_array = input().split(' ')
    proc = work_array[0]
    result = ""
    print(number_array)
    print(name_array)
    if proc == "make":
        number_array.append(work_array[1])
        name_array.append(work_array[2])
    elif proc == "getnum":
        result = getnum(int(work_array[1]) - 1)
        print(result)
    elif proc == "getname":
        result = getname(int(work_array[1]) - 1)
        print(result)