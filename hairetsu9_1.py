# 配列のスライス記法処理
# 新規作成 2023/3/7
# 配列のスライス記法による要素の操作

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# nums[2:5] = [100, 200, 300]
# sliced_list = nums[2:5]

sliced_list1 = nums[2:8:2]
sliced_list2 = nums[8:2:-2]
sliced_list3 = nums[::-1]
sliced_list4 = nums[::-2]

print(nums)
print(sliced_list1)
print(sliced_list2)
print(sliced_list3)
print(sliced_list4)
