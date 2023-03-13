# カレンダライブラリ
# 新規作成 2023/3/13

import calendar

# カレンダ型
calendar.setfirstweekday(6)
calendar.setfirstweekday(calendar.SUNDAY)
calen = calendar.month(2001,1)
print(calen)

# リスト型
cal_data = calendar.monthcalendar(2001,1)
print(cal_data)

# うるう年判定
print(calendar.isleap(2000))
print(calendar.isleap(2001))
