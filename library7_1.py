# 日付の表現方法
import datetime

birthday = datetime.datetime(year=2000, month=4, day=11)
print(birthday)

# 年
print(birthday.year)
# 月
print(birthday.month)
# 日
print(birthday.day)
# 時間
print(birthday.hour)
# 分
print(birthday.minute)
# 秒
print(birthday.second)
# 曜日
print(birthday.weekday())
# Bが月、dが日付、Aが曜日、Yが年
b1=birthday.strftime("%B %d %A %Y")
print(b1)
