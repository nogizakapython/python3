target = input()

n = int(input())
users = {}
for i in range(n):
    tmp = input().split()

    users[tmp[0]] = tmp[1]

m = int(input())
fortunes = {}
for i in range(m):
    tmp = input().split()

    fortunes[tmp[0]] = tmp[1]

user_blood = None
for user, blood in users.items():
    if user == target:
        user_blood = blood
        break

for blood, fortune in fortunes.items():
    if blood == user_blood:
        print(fortune)
        break
