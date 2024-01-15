###########################
## ユークリッドの互除法
##########################

M, N = map(int, input("MとNを、M Nの形式で入力してください\n").split())
if M < N:
  M, N = N, M

while N != 0:
  M, N = N, M % N

print(M)
