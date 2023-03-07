# タプルをアンパックする
# 新規作成 2023/3/7

tokyo = ("JPY", 36, 140)
# タプルのアンパック(変数をそれぞれ定義する)
currency,lat,long = tokyo
print(currency)
print(lat)
print(long)

# 使う文字を減らす場合は「_」を使う
_,lat1,long1 = tokyo
print(lat1)
print(long1)

osaka = "JPY",35,135
# タプルの要素をまとめて1つの変数にするには「*」を使う。
current,*location = osaka
print(current)
print(location)

naha = "JPY",27,126
current,*_ = naha
print(current)
print(naha)


