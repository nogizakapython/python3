# datetimeライブラリ
# 新規作成 2023/3/13
# datetimeライブラリを読み込む
import datetime

# 現在の日付を表示する
now = datetime.datetime.now()
print(now)

# 2000年4月1日を表示する
birthday = datetime.datetime(year=2000,month=4,day=11)
print(birthday)

# 1993年8月20日を表示する
birthday2 = datetime.datetime.strptime("1993-08-20","%Y-%m-%d")
print(birthday2)

# 1992年8月20日を表示する
birthday3 = datetime.datetime.strptime("1992-08-20","%Y-%m-%d")
print(birthday3)

