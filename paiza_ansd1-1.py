S, A, T = map(int,input().split()) #入力

Already_downroad = T*A #ダウンロードが終わったファイルのデータ量の総和
All_downroad = S*A #全てのファイルのデータ量の総和

print((100 * Already_downroad) // All_downroad)
