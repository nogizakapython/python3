#入力するデータ数とスペース埋めで何桁で出力するか入力する
data1 = input("数値のデータの数とスペース埋めで何桁の数に指定するかスペース区切りで入力してください")
array1 = data1.split(' ')
N = int(array1[0])
keta = int(array1[1])
for i in range(0,N):
    num = input()
    ans = "{: >{}}".format(num,keta)
    print(ans)
