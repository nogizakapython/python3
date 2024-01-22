##############################
#####  糸魚川             ####
##############################

import datetime
import random
date1 = datetime.datetime.now()

str1 = input("文字を入力してください\n")
date2 = date1.strftime('%Y%m%d')
str2 = str1 + date2
print(str2)
array1 = ["秋元真夏","長濱ねる","矢久保美緒","与田祐希","影山優佳","遠藤さくら"]
num = random.randint(0,len(array1)-1)
c1 = array1[num]

ans = "糸魚川の今日のオナニーの相手は" + c1 + "です"
print(ans)
