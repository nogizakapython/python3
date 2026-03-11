N, M = map(int,input().split())

LED = [0] * N #明るさを管理する配列

for i in range(M):
    a, b = map(int,input().split())
    LED[a - 1] = b
    #すべてのランプが点灯→全てのランプの明るさが正ならば、総和を出力し繰り返し処理を止める
    if min(LED) > 0:
        print(sum(LED))
        break