# 入力用配列
w_array1 = input().split(' ')
#データ成型用配列
array1 = []
#入力用に入れた配列の要素をデータ成型用配列に代入する
for i in w_array1:
    array1.append(int(i))
# 昇順に並べる
array2 = sorted(array1)
# 要素の一番小さい配列を削除する
array2.pop(0)
# 配列の要素数を取得する。
leng1 = len(array2)
# 配列の要素が一番大きい値を削除する
array2.pop(leng1-1)
# 配列の要素の合計を計算する。
print(sum(array2))
