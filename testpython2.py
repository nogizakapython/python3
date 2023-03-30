# Linux用Python3プログラム
# 新規作成 2023/3/30

array1 = {"秋元真夏": 90,"池田瑛紗": 100,"白石麻衣": 40,"弓木奈於": 10}


keys_sorted1 = sorted(array1.items())
print(keys_sorted1)

keys_sorted2 = sorted(array1.keys())
print(keys_sorted2)

keys_sorted3 = sorted(array1.items(),key=lambda a:a[1])
print(keys_sorted3)


