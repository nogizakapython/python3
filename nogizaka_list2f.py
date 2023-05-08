# 乃木坂写真集リストの関数モジュール
# 新規作成 2023/4/7

member_list = ['梅澤美波','山下美月','賀喜遥香','与田祐希']
msg1 = "メンバーではありません"

class BookItem:
    def __init__(self,name,title, price):
        self.name = name
        self.title = title
        self.price = price

    def info(self):
        return self.name + ':' + self.title + ': ¥' + str(self.price)
      
    def membercheck(self):
        if self.name in member_list:
          return self.name + "は乃木坂メンバーです。「" + self.title + "」は" + str(self.price) + "円で発売中です"
        else:
          return msg1   
    
    def send_info(self):
        print("5冊以上購入すると送料無料です")  

    def get_total_price(self, count):
        total_price = self.price * count
        send_price = 500
        # 5冊以上購入した場合は送料無料
        if count < 5:
            total_price += send_price 
        
        return round(total_price)
