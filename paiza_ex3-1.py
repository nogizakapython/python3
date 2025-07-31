H, M = map(int,input().split())
if 7 <= H <= 12: #7時台から12時台ならば、昼ごはん
    print("lunch")
elif 13 <= H <= 18: #そうでなく13時台から18時台ならば、晩ごはん
    print("dinner")
else: #いずれの条件を満たさないなら、朝ごはん
    print("breakfast")
