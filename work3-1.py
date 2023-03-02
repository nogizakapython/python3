# 複数の入力を配列に入れる
# 新規作成 2023/3/2
str1 = input()
s = str1.rstrip().split(' ')
for i in range(len(s)):
  print(s[i])
