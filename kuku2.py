#####################################
###     インド式九九の一覧表作成
#####################################


startn = 1
endn = 21

# スペース関数
def space1():
  print()

# 罫線関数
def div1():
  print("=" * (3*20 + 3* (20-1)))

for i in range(startn,endn):
  for j in range(startn,endn):
    ans = i * j
    if j == 20:
      print("{:>3}".format(ans),end="")
    else:
      print("{:>3}".format(ans),end=" | ")

  if i < 20:
    space1()
    div1()
