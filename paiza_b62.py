target_name = input()
n = int(input())
dict1 = {}
for i in range(n):
    key,value = input().split(' ')
    dict1[key] = value
for str1 in dict1.keys():
    if str1 == target_name:
        ans1 = dict1[target_name]
        print(str1 + " " + ans1)
