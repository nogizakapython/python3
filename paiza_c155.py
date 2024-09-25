# reモジュールの呼び出し
import re

# 検索する文字列を入力する
str1 = input()
# 検索回数を入力する
n = int(input())

for i in range(n):
    # 検索元文字列を入力する
    target_word = input()
    # 部分一致したら「Yes」、一致しなかったら「No」を出力
    flag1 = re.search(str1,target_word)
    if flag1:
        print("Yes")
    else:
        print("No")
