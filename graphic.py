import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def plot_currency(currency, db_path="data/currency.db"):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(
        "SELECT date, rate FROM currency_rates WHERE currency = ? ORDER BY date ASC",
        conn,
        params=(currency,)
    )
    conn.close()

    df["date"] = pd.to_datetime(df["date"])

    plt.figure(figsize=(10, 5))
    plt.plot(df["date"], df["rate"], label=currency, linewidth=2)
    plt.title(f"Динамика курса {currency}")
    plt.xlabel("Дата")
    plt.ylabel("Курс к RUB")
    plt.legend()
    plt.grid(True)

    plt.savefig('graphics\cur.png')
    plt.show()