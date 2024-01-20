###########################
## トリボナビッチ数列
##########################

def tri_r(num):
  if num <= 1:
    return 0
  if num == 2:
    return 1
  return(tri_r(num - 1) + tri_r(num - 2) + tri_r(num - 3))

ans = tri_r(7)
print(ans)

