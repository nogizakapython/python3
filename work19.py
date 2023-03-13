# 配列をシャッフルして勝者を一人取り出す
# 新規作成

import random

count = 3
i = 0
names = ["Ichiro","Shohei","Roki"]
result = [0,0,0]


while i in range(0,count):
  str = random.choice(names)
  if str == "Ichiro":
    result[0] += 1
  elif str == "Shohei":
    result[1] += 1
  elif str == "Roki":
    result[2] += 1
  i += 1


for j in result:
  print(f"{names[j]}は{result[j]}回勝ちました")
