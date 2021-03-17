from bs4 import BeautifulSoup
import requests
from time import time, sleep
from twilio.rest import Client
import config


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

main_url = 'https://finance.yahoo.com/quote/GME/'
response = requests.get(main_url)
soup = BeautifulSoup(response.text, "html.parser")

price = soup.find("span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
price_change = soup.find("span", {"class": "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)"}).text

pc = price_change.split(' ')[1]

new_pc = pc[pc.find("(")+1:pc.find(")")]


def p2f(x):
     return float(x.strip('%'))/100

print(p2f(new_pc))
price = float(price)
print(price)
print(price_change)
print(new_pc)
price_change_alert = .05

if float(price) < price_change_alert:
    message = client.messages \
                .create(
                     body="Today's closing price is {price}, and the change is {price_change}",
                     from_='+16072142415',
                     to='+16304181900'
                )
      
    print(message.sid)

