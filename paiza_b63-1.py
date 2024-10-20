import sys

target = input()
n = int(input())
dictionary = {}

for i in range(n):
    tmp = input().split()
    dictionary[tmp[0]] = tmp[1]

for blood, fortune in dictionary.items():
    if blood == target:
        print(fortune)
        break
