n = int(input())

for i in range(n):
    s = input()

    hash = 0
    for j in range(len(s)):
        hash += (j+1) * (ord(s[j])-ord('a')+1)

    hash %= 100

    print(hash)
