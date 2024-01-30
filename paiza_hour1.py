data = input()
array1 = data.split('/')
year = array1[0]
month = array1[1]
day = array1[2]
data2 = array1[3]
array2 = data2.split(":")
hour = array2[0]
minute = array2[1]

print(year)
print(month)
print(day)
print(hour)
print(minute)
