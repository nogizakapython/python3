
# HTMLファイル起動パッケージ
import subprocess
# powerpointファイル編集、読み込みパッケージ
import aspose.slides as slides

# ファイル名
file_name = "プレゼンテスト2.pptx"
pres = slides.Presentation(file_name)

# PPTからHTMLに変換パッケージを読み込む
controller = slides.export.ResponsiveHtmlController()
htmlOptions = slides.export.HtmlOptions()
htmlOptions.html_formatter = slides.export.HtmlFormatter.create_custom_formatter(controller)

# 出力ファイル
output_file = "index.html"
pres.save(output_file, slides.export.SaveFormat.HTML, htmlOptions)
    
# windowsから起動する
subprocess.run(['start', output_file], shell=True)