#######################
#   小数表示テスト
########################

input_line = input("小数と小数点以下表示したい桁数を入力してください\n")
array1 = input_line.split(' ')
N = float(array1[0])
M = int(array1[1])
ans = '{:.{}f}'.format(N,M)
print(ans)
