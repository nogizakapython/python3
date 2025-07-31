A = list(map(int,input().split()))
T = list(map(str,input().split()))

Already_downroad = 0 #ダウンロードが終わったファイルのデータ量の総和を管理する変数
All_downroad = sum(A) #全てのファイルのデータ量の総和

for i in range(5):
    if T[i] == "o": #もしファイルのダウンロードが終わっているならば、データ量をAll_downloadに足す
        Already_downroad += A[i]

print((100 * Already_downroad) // All_downroad)
