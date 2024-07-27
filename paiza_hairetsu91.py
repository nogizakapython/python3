num = int(input())
S = [int(x) for x in input().split()]
S = list(set(S))
length1 = len(S)
for i in range(length1):
    if i == length1 - 1:
        print(S[i],end="")
    else:
        print(S[i],end=" ")
