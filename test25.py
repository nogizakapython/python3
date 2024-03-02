from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://flora-inc.co.jp/page/company.php"
ignores = ["事業内容", "事業所所在地"]

def scraping():
    soup = BeautifulSoup(urlopen(url).read().decode(), 'html.parser')
    table = soup.find('table')
    for tr in table.findAll('tr'):
         title = tr.find("td", {"class", "title"}).text
         if title in ignores:
            continue
         contents = tr.findAll("td", {"class", "content"})
         yield title, *[content.text for content in contents]

def main():
    for row in scraping():
        print(*[f'"{col}"' for col in row], sep=",")

if __name__ == "__main__":
    main()
