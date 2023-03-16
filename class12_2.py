# staticmethod
# NogizakaHelper class
# 新規作成 2023/3/16

class NogizakaHelper:
   @staticmethod
   def to_h1(str):
        return f"<h1>{str}</h1>"
   @staticmethod
   def to_h2(str):
        return f"<h2>{str}</h2>"

   @staticmethod
   def to_p(str):
        return f"<p>{str}</p>"

print(NogizakaHelper.to_h1("乃木坂メンバー"))
print(NogizakaHelper.to_h2("梅澤美波"))
print(NogizakaHelper.to_p("乃木坂46のキャプテンです。"))
