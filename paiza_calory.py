t_cal = int(input())
data = input()
array1 = data.split(' ')
count1 = len(array1)
sum_cal = 0
for i in range(count1):
    data1 = int(array1[i])
    sum_cal += data1

if sum_cal <= t_cal:
    print("OK")
else:
    print("NG")
