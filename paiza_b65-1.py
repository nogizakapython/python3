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

for user, user_blood in users.items():
    for blood, fortune in fortunes.items():
        if user_blood == blood:
            print(user + " " + fortune)
            break
