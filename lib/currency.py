import requests 
if __name__ == "__main__":
    pass


def get_currency(URL):
    responce = requests.get(URL)
    currencies = responce.json()
    for currency in currencies:
        print(currency['ccy'], " ", currency['base_ccy'], " | ", currency['buy'], " ", currency['sale'])