import sys



try:
    weight = float(input("体重を(kg)で整数または小数で入力してください"))
    if weight < 0:
        raise ValueError
except ValueError as e:
    print("整数または小数で入力してください")
    sys.exit()
  
try:
    tall = float(input("身長を(m)で小数点で入力してください"))
    if tall < 0:
        raise ValueError
except ValueError as e:
    print("整数または小数で入力してください")
    sys.exit()    

bmi = weight / pow(tall,2)

bmi = round(bmi,2)

print(bmi)

