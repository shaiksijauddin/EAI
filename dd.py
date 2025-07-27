import sqlite3
import pandas as pd

conn = sqlite3.connect("india_trade.db")
df = pd.read_sql("SELECT * FROM trade_data LIMIT 5;", conn)
print(df.head())
