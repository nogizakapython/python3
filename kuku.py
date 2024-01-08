#####################################
###     九九の一覧表作成
#####################################


startn = 1
endn = 10

# スペース関数
def space1():
  print()

# 罫線関数
def div1():
  print("=" * (2*9 + 3* (9-1)))

for i in range(startn,endn):
  for j in range(startn,endn):
    ans = i * j
    if j == 9:
      print("{:>2}".format(ans),end="")
    else:
      print("{:>2}".format(ans),end=" | ")

  if i < 9:
    space1()
    div1()
