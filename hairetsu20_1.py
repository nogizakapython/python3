# 変数の挙動
# 新規作成 2023/3/9

nums = [10, 20, 30]
# 指し示す場所をコピーする
nums_bak = nums
# 配列をコピーする
nums_bak1 = nums.copy()
nums[0] = 100

print(nums)
print(nums_bak)
print(nums_bak1)
