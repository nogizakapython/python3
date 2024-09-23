n = int(input())  # 1つ目の入力は使わないので読み飛ばす
strings = input().split()
nums = []

for num in strings:
    nums.append(int(num))

nums.sort()

for i in nums:
    print(i)
