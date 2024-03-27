N = int(input())
number = str(N)
str_length = len(number)
sum1 = 0
for i in range(str_length):
    data = int(number[i])
    sum1 += data
print(sum1)
