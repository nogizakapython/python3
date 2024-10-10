num = int(input())
array1 = [int(x) for x in input().split(' ')]
leng1 = len(array1)
ans = int(input())
for i in range(leng1):
    a = array1[i]
    if a == ans:
        print(i+1)
