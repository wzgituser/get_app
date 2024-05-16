import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()


def get_crypto():
    list_a = []
    title = input("Crypto-currency rate checker to start type Y/N:" )
    if title == "Y" or "yy":

        a = requests.get('https://api.coincap.io/v2/assets/').json()

        for item in a["data"]: 
                print(item["id"])

        bb = input("choice one from the list above and type chosen one to check current price:")

        c = f'https://api.coincap.io/v2/assets/{bb}'

        cc = c
        b = requests.get(cc).json()
        bB = requests.get(cc)
        print(bB)
        if b :
            rank = b["data"]["rank"]
            symbol = b["data"]["symbol"]
            name_val = b["data"]["name"]
            price_val = b["data"]["priceUsd"]
            print(f'\n rank:{rank} \n {symbol} \n name: {name_val} \n price: {price_val} of usd')
        else:
             print("name error, type corect one")
    else:
         print("try again")

if __name__ =="__main__":
    get_crypto()

