# mailテンプレートテスト

import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application")

mail = outlook.CreateItem(0)

mail.to = 'hattori201910@gmail.com'
mail.cc = 'east201110@yahoo.co.jp'
mail.bcc = 'nogizakapython@outlook.jp'
mail.subject = 'test'
mail.bodyFormat = 1
mail.body = '''テストメールです。'''

mail.display(True)
