# 3で割り切れる要素を取り除く
# 新規作成 2023/3/8

nums = [1,2,3,4,5,6,7,8,9,10]

# リスト内包で3で割った余りが0の要素を除外する
nums1 = [num for num in nums if num % 3 != 0]


for data in nums1:
  print(data)