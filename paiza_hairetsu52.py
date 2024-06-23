num = int(input())

for i in range(num):
    x,y=map(int,input().split(' '))
    x_d = abs(x-2)
    y_d = abs(y-3)
    d = x_d + y_d
    print(d)
