import pandas as pd
from decimal import Decimal

usd = pd.read_excel('data/USD.xlsx')
eur = pd.read_excel('data/EUR.xlsx')

usd['currency'] = 'USD'
eur['currency'] = 'EUR'

currencies_df = pd.concat([usd, eur], ignore_index=True)
currencies_df['curs'] = currencies_df['curs'].astype(str).str.replace(',', '.').apply(Decimal)