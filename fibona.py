###########################
## フィボナッチ数列
##########################

def fib_r(num):
  if num <= 1:
    return num
  return(fib_r(num - 1) + fib_r(num - 2))

ans = fib_r(10)
print(ans)

