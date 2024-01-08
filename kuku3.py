#####################################
###     九九の一覧表作成
#####################################

#各段の変数定義
startn = 1
endn = 10
#桁数変数の定義
keta = 2
# スペース関数
def space1():
  print()

# 罫線関数
def div1():
  print("=" * (keta*(endn - startn) + 3 * (endn - startn -1)))

for i in range(startn,endn):
  for j in range(startn,endn):
    ans = i * j
    if j == 9:
      print(f"{ans:>{keta}}",end="")
    else:
      print(f"{ans:>{keta}}",end=" | ")

  if i < 9:
    space1()
    div1()
