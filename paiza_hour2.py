data = input()
array1 = data.split(' ')
ymd = array1[0]
hm = array1[1]
array2 = ymd.split('/')
year = array2[0]
month = array2[1]
day = array2[2]
array3 = hm.split(':')
hour = array3[0]
minute = array3[1]
print(year)
print(month)
print(day)
print(hour)
print(minute)
