N,D=map(int,input().split())
X,Y=map(int,input().split())
d_count = 0
for i in range(D):
  A,B=map(int,input().split())
  X_dis = X - A
  Y_dis = Y - B
  if X_dis < 0:
    X_dis *= -1
  if Y_dis < 0:
    Y_dis *= -1
  if X_dis + Y_dis <= D:
    d_count += 1

print(d_count)



