num = int(input())
for i in range(num):
    data = input()
    array2 = list(map(int,data.split(' ')))
    print(sum(array2) - array2[0])
