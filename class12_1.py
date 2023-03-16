# staticmethod
# 新規作成 2023/3/16

class HtmlHelper:
   @staticmethod
   def to_h1(str):
        return f"<h1>{str}</h1>"
   @staticmethod
   def to_p(str):
        return f"<p>{str}</p>"

print(HtmlHelper.to_h1("Hello"))
print(HtmlHelper.to_p("wow"))
