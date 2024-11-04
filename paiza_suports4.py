# 数値入力
n = int(input())
# Dictionaryの定義
dict1 = {}
# listの定義
list1 = []
# 標準入力からdict1にkeyとvalueを入れる
for i in range(n):
    key,value = input().split(' ')
    dict1[key] = value
# dict1のkeyをlist1に入れる
for number in dict1.keys():
    list1.append(int(number))
# list1を昇順に並び替える
list1.sort()
# listの要素を取り出し、dict1のkeyと合わせて出力
for num in list1:
    print(str(num) + " " + dict1[str(num)] )
