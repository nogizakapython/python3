##############################
#####  糸魚川             ####
##############################

import datetime
import random
date1 = datetime.datetime.now()

str1 = input("文字を入力してください\n")
date2 = date1.year
str2 = str1 + str(date2)

array1 = ["秋元真夏","長濱ねる","矢久保美緒"]
num = random.randint(0,len(array1)-1)
c1 = array1[num]

ans = str2 + c1
print(ans)
