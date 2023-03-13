# 日付の表現方法
# 東関東大震災の日付表現
# 新規作成 2023/3/13
import datetime

birthday = datetime.datetime(year=2011, month=3, day=11,hour=14,minute=46,second=21)
print(birthday)

print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.hour)
print(birthday.minute)
print(birthday.second)
# 曜日
print(birthday.weekday())
j_earthquake = birthday.strftime('%B %d %A %Y')
print(j_earthquake)
