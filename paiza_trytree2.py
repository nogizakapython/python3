num = int(input())
array1 = []
seen = set()  # すでに登録した接頭辞を記録するセット

for i in range(num):
    s1 = input()
    prefix = ""
    for j in s1:
        prefix += j
        # セットで存在チェックを行う（一瞬で終わります）
        if prefix not in seen:
            seen.add(prefix)
            array1.append(prefix)

array1.sort()            
for k in array1:
    print(k)