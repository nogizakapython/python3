# 数値の0埋めテスト
# create 2024/1/6
num = input()
# 0埋め
ans = format(num,"0>3")
print(ans)
# 0埋め
ans2 = num.zfill(3)
print(ans2)
