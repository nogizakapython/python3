# 配列のスライス記法処理
# 新規作成 2023/3/7

nums = [1,2,3,4,5,6,7,8,9]

nums[2:4] = [30,40]

print(nums)

nums[3:]=[]
print(nums)

nums.clear

nums = [1,2,3,4,5,6,7,8,9]
nums[:5] = []
print(nums)
