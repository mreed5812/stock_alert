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

