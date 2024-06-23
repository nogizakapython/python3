n = int(input())
array1 = list(map(int,input().split(' ')))
a_sum = sum(array1)
a_avg = a_sum / n

for i in array1:
    if i >= a_avg:
        print(i)
