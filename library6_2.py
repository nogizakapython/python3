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

# 2000年4月1日を表示する
s_birthday = datetime.datetime(year=1994,month=5,day=15,hour=17,minute=7,second=25)
print(s_birthday)

# 2000年4月1日を表示する
n_birthday = datetime.datetime.strptime('1998-01-25','%Y-%m-%d')
print(n_birthday)
