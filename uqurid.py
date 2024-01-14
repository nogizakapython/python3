###########################
## ユークリッドの互除法
##########################

input_line1 = input("MとNを、M Nの形式で入力してください\n")
array1 = input_line1.split(' ')
M = int(array1[0])
N = int(array1[1])
if M < N:
  tmp = N
  N = M
  M = tmp

while True:
  d = M % N
  if d == 0:
    print(N)
    break
  M = N
  N = d



