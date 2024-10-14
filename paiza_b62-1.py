target = input()
n = int(input())
dictionary = {}

for i in range(n):
    tmp = input().split()
    dictionary[tmp[0]] = tmp[1]

for user, blood in dictionary.items():
    if user == target:
        print(user + " " + blood)
        break
