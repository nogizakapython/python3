# copyライブラリを使う
# 新規作成 2023/3/15

# copyライブラリをimportする
import copy
nums = [10, 20, 30]

nums_bak = nums.copy()
nums[0] = 100
nums.append(40)

print(nums)
print(nums_bak)

nums2 = [10,20,30,[40,50]]
# mutableデータはcopyライブラリのdeepcopy関数を使う
nums_bak2 = copy.deepcopy(nums)
nums2[3][0] = 100
print(nums2)
print(nums_bak2)


