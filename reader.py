import pandas as pd
from decimal import Decimal
import sqlite3

def load_to_db(db_path="data/currency.db"):
    usd = pd.read_excel("data/USD.xlsx")
    eur = pd.read_excel("data/EUR.xlsx")

    usd["currency"] = "USD"
    eur["currency"] = "EUR"

    df = pd.concat([usd, eur], ignore_index=True)
    df["curs"] = df["curs"].astype(str).str.replace(",", ".").apply(Decimal)
    df["data"] = pd.to_datetime(df["data"], format="%d.%m.%Y").dt.date

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS currency_rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            rate DECIMAL(10,4),
            currency TEXT
        )
    """)

    cursor.execute("DELETE FROM currency_rates")  # очистим для теста
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO currency_rates (date, rate, currency)
            VALUES (?, ?, ?)
        """, (row["data"], float(row["curs"]), row["currency"]))

    conn.commit()
    conn.close()
    print("Данные загружены в БД")
