N,M = map(int,input().split(" "))
w = int(input())
Nweight = N 
count = 1
while Nweight <= 1500:
    dif = abs(w-Nweight)
    print(str(Nweight) + " " + str(dif))
    count += 1 
    Nweight = N * count