S = [0] * 5
values = input().split()
for i in range(5):
    S[i] = values[i]

sorted_S = sorted(S)

for s in sorted_S:
    print(s)
