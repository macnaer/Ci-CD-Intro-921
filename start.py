from lib.currency import get_currency


URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
get_currency(URL)