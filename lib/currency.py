import requests
if __name__ == "__main__":
    pass


def get_currency(URL):
    responce = requests.get(URL)
    currencies = responce.json()
    for currency in currencies:
        print(currency['ccy'], " ", currency['base_ccy'],
              " | ", currency['buy'], " ", currency['sale'])

    file = open('currency.txt', 'w')
    for item in currencies:
        file.write(item["ccy"] + " " + item["base_ccy"] + " " +
                   item["buy"] + " | " + item["sale"]+"\n")
    file.close
    print("Saved in file ", file)
