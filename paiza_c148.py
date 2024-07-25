num = int(input())
hour = 0
minute = 0
wt = 0
for i in range(num):
    data = input()
    t_array = data.split(' ')
    time1 = t_array[0]
    d_array = time1.split(":")
    hour1 = int(d_array[0])
    minute1 = int(d_array[1])
    wm1 = hour1 * 60 + minute1
    time2 = t_array[1]
    d_array = time2.split(":")
    hour2 = int(d_array[0])
    minute2 = int(d_array[1])
    wm2 = hour2 * 60 + minute2
    wm = wm2 - wm1
    wt += wm
hour = str(int(wt / 60))
minute = str(wt % 60)
print(hour + " " + minute)
