# 日付の計算処理
# 新規作成 2023/3/13
# datetimeライブラリのインポート
import datetime

day1 = datetime.datetime(year=2000, month=4, day=11)
day2 = datetime.datetime(year=2001, month=1, day=1)

# 日付の差を計算する
diff = day2 - day1 #timedelta
# 秒に変換する
diff_seconds = diff.total_seconds()
# 日に変換する
diff_days = diff_seconds / (60 * 60 * 24)
print(diff_seconds)
print(diff_days)

# 3日と5時間後を計算する
delta = datetime.timedelta(days=3,hours=5)
day3 = day1 + delta
print(day3)
