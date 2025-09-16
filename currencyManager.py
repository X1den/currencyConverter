from enum import Enum

class CurrencyCode(Enum):
    USD = 'USD'
    RUB = 'RUB'
    EUR = 'EUR'

class OperationType(Enum):
    BUY = 'BUY'
    SELL = 'SELL'

class CurrencyManager:
    def __init__(self, df):
        self.df = df

    def dateCreate(self):
        print(self.df.head())
        import sqlite3
        conn = sqlite3.connect('data/currency.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS currency_rates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                rate DECIMAL(10,4),
                currency TEXT
            )
        ''')
        for _, row in self.df.iterrows():
            cursor.execute('''
            INSERT INTO currency_rates (date, rate, currency)
            VALUES (?, ?, ?)
            ''', (row['data'], row['curs'], row['currency']))
        conn.commit()
        conn.close()

# Использование
manager = CurrencyManager(currencies_df)
manager.dateCreate()
