n = int(input())
dict1 = {}
for i in range(n):
    k,v = input().split(' ')
    dict1[k] = v

for key,value in dict1.items():
    print(key + " " + value)
