import sqlite3
from decimal import Decimal, getcontext
from manager import CurrencyCode

getcontext().prec = 10

class Converter:
    def __init__(self, db_path="data/currency.db"):
        self.db_path = db_path

    def _get_rate(self, currency, date):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT rate FROM currency_rates
            WHERE currency = ? AND date = ?
        """, (currency.value, date))
        row = cursor.fetchone()
        conn.close()
        if not row:
            raise ValueError(f"Нет курса {currency.value} на дату {date}")
        return Decimal(str(row[0]))

    def convert(self, amount, from_currency: CurrencyCode, to_currency: CurrencyCode, date):
        if from_currency == to_currency:
            return amount

        from_rate = self._get_rate(from_currency, date)
        to_rate = self._get_rate(to_currency, date)

        rub_amount = amount * from_rate
        result = rub_amount / to_rate
        return result.quantize(Decimal("0.0001"))