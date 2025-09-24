from reader import load_to_db
from converter import Converter
from manager import CurrencyCode
from graphic import plot_currency
from decimal import Decimal

load_to_db()
conv = Converter()

amount = Decimal("100")
date = "2025-09-16"
result = conv.convert(amount, CurrencyCode.USD, CurrencyCode.EUR, date)
print(f"{amount} USD = {result} EUR на {date}")

plot_currency("USD")
plot_currency("EUR")