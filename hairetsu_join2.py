# 配列から要素を取り出し、結合する処理
#  新規作成  2023/4/7

# join関数を使う場合
array1 = ['サヨナラの意味','僕たちのサヨナラ','ハルジオンが咲く頃']

str1 = ",".join(array1)
str2 = ""

print(str1)


# join関数を使わない場合

count = 0
for word in array1:
    if count > 0:
        str2 = str2 + "," + word
    else:
        str2 = str2 + word    
    count += 1

print(str2)