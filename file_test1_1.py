# ファイルの書き込み処理
# 新規作成 2023/3/14

file_name = "file_test2.txt"

try:
  f = open(file_name,mode="a")
  f.write("秋元真夏\n")
except:
  print("失敗")
print("成功")
f.close()
