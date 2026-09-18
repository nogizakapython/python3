e = 100
table = [[] for i in range(e)]

a,b = map(int,input().split())

n = int(input())

for i in range(n):
    p,d = map(int,input().split())
    hash = 0
    if p == 1:
        hash = (a * d + b) % 100
        table[hash].append(d)
    elif p == 2:
        count = 0
        for j in range(e):
            if d in table[j]:
                count += 1
        if count == 0:
            print("No")
        else:
            print("Yes")        


for k in range(len(table)):
    print(" ".join(map(str, table[k])))