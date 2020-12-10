import requests
from bs4 import BeautifulSoup
import time
import smtplib

URL = 'https://www.amazon.co.uk/Nike-Unisex-Adults-Essential-Running/dp/B07ZTTQXXT/ref=sr_1_1?crid=3SHAZ3MMSL57Q&dchild=1&keywords=nike+air+max+95+mens+black&qid=1607613393&quartzVehicle=99-1304&replacementKeywords=nike+air+max+mens+black&sprefix=nike+air+max+95+mens+%2Caps%2C153&sr=8-1'
HEADERS = {"User-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
WANTED_PRICE = 150
EMAIL_ADDRESS = 'Neilfoster81@gmail.com'

def trackPrice():
    price = int(getPrice())
    if price > WANTED_PRICE:
        diff = price - WANTED_PRICE
        print(f"Still £{diff} too expensive")
    else:
        print("Cheaper!")
        sendMail()
       


def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()[1:4]
    print(title)
    print(price)
    return price

def sendMail():
    subject = "Amazon Price Dropped!"
    mailtext='Subject:'+subject+'\n\n'+URL

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, 'APP_PASSWORD')
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, mailtext)
    print("Sent email")

if __name__ == "__main__":
    while True:
        trackPrice()
        time.sleep(2)