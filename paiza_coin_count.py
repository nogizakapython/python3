array1 = [500,100,50,10,5,1]
coin_count = 0
cost = 0

n = int(input())
cost = n
for coin in array1:
  ans = int(cost / coin)
  if ans >= 1:
    coin_count += ans
    cost -= ans * coin

print(coin_count)
