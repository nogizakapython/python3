C = int(input())
M = int(input())

D = int(M / 30)
X = (M % 30)

if X > 0:
  D += 1

print(C * D)
