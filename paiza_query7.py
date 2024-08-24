n,k = map(int,input().split(' '))
dic1 = {x:y for x,y in [input().split(' ') for _ in range(n)]}

for t in range(k):
    array1 = input().split(' ')
    leng1 = len(array1)
    key = array1[1]
    if leng1 == 3:
        value = array1[2]
        dic1[key] = value
    elif leng1 == 2:
        word = array1[0]
        if word == "call":
            key = array1[1]
            print(dic1[key])
        else:
            dic1.pop(key)
