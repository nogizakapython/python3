N = int(input())
S = input()

count = {chr(x): 0 for x in range(ord("a"), ord("z")+1)}
for char in S:
    count[char] += 1

print(" ".join(map(str, count.values())))
