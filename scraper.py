import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.co.uk/Nike-Unisex-Adults-Essential-Running/dp/B07ZTTQXXT/ref=sr_1_1?crid=3SHAZ3MMSL57Q&dchild=1&keywords=nike+air+max+95+mens+black&qid=1607613393&quartzVehicle=99-1304&replacementKeywords=nike+air+max+mens+black&sprefix=nike+air+max+95+mens+%2Caps%2C153&sr=8-1'
HEADERS = {"User-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
PRICE = 140


def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    print(title)

if __name__ == "__main__":
    getPrice()