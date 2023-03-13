# 日付の計算処理
# 新規作成 2023/3/13
# datetimeライブラリのインポート
import datetime

day1 = datetime.datetime(year=1992, month=8, day=20)
day2 = datetime.datetime(year=1993, month=8, day=20)

# 日付の差を計算する
diff = day2 - day1 #timedelta
# 秒に変換する
diff_seconds = diff.total_seconds()
# 日に変換する
diff_days = diff_seconds / (60 * 60 * 24)
print(diff_seconds)
print(diff_days)

# 180日後をを計算する
delta = datetime.timedelta(days=184)
day3 = day1 + delta
print(day3)

day4 = datetime.datetime(year=1993, month=2, day=20)
diff2 = day4 - day1
diff3 = day2 - day4
diff_seconds2 = diff2.total_seconds()
diff_seconds3 = diff3.total_seconds()
# 日に変換する
diff_days2 = diff_seconds2 / (60 * 60 * 24)
print(diff_seconds2)
print(diff_days2)
# 日に変換する
diff_days3 = diff_seconds3 / (60 * 60 * 24)
print(diff_seconds3)
print(diff_days3)
