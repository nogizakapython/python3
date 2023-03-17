from datetime import datetime,timedelta,timezone

jst = timezone(timedelta(hours=9))
today = datetime.now(jst)
print(today)
