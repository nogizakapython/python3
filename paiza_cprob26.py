n,a,b = map(float,input().split(" "))
ans = n 
ans = ans - ((ans * a) / 100)
ans = ans - ((ans * b) / 100)
print(ans)