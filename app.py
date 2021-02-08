from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from time import time, sleep
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACeed1ff514f0d12ffec41f02d77eb99bf'
auth_token = 'daffe7a17fa93585d4fb6052405e5a00'
client = Client(account_sid, auth_token)

main_url = 'https://finance.yahoo.com/quote/GME/'
response = requests.get(main_url)
soup = BeautifulSoup(response.text, "html.parser")

price = soup.find("span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text

price = float(price)
print(price)

if price < 70:
    message = client.messages \
                .create(
                     body="Price is less than $70",
                     from_='+16072142415',
                     to='+16304181900'
                )
      
    print(message.sid)

