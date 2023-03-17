from datetime import datetime,timedelta,timezone

jst = timezone(timedelta(hours=9))
today = datetime.now(jst)
print(today)

print(today.year)
print(today.month)
print(today.day)

day = datetime.strptime("2030/01/10 06:02:19","%Y/%m/%d %H:%M:%S")
print(day)
