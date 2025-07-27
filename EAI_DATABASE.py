import pandas as pd
import numpy as np
import sqlite3
from pathlib import Path

# Load and preprocess the data
print("Loading and preprocessing data...")
df = pd.read_csv('EAI.csv')

# Data Cleaning
df = df.dropna(subset=['Country'], how='all')

# Convert numeric columns
numeric_cols = ['Export', 'Import', 'Total Trade', 'Trade Balance']
for col in numeric_cols:
    df[col] = df[col].astype(str).str.replace(',', '')
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# Fill remaining NaNs
df = df.fillna(0)

# Create Year column
df['Year'] = df['Financial Year(start)'].astype(str).str.extract('(\d+)')[0].fillna(0).astype(int)

# Add India's perspective columns
df['India_Imports'] = df['Export']  # Other countries' exports to India
df['India_Exports'] = df['Import']  # Other countries' imports from India
df['India_Trade_Balance'] = df['India_Exports'] - df['India_Imports']

# SQLite Database Setup
db_path = 'india_trade.db'
print(f"\nCreating SQLite database at {db_path}...")

# Connect to SQLite (this will create the database if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create main table
cursor.execute('''
CREATE TABLE IF NOT EXISTS trade_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country TEXT,
    year INTEGER,
    export REAL,
    import REAL,
    total_trade REAL,
    trade_balance REAL,
    india_imports REAL,
    india_exports REAL,
    india_trade_balance REAL,
    financial_year_start TEXT,
    financial_year_end TEXT
)
''')

# Insert data
print("Inserting data into SQLite...")
df.to_sql('trade_data', conn, if_exists='replace', index=False)

# Create indexes
print("Creating indexes for better performance...")
cursor.executescript('''
CREATE INDEX IF NOT EXISTS idx_country ON trade_data(country);
CREATE INDEX IF NOT EXISTS idx_year ON trade_data(year);
CREATE INDEX IF NOT EXISTS idx_trade_balance ON trade_data(india_trade_balance);
''')

# Create views
print("Creating analytical views...")
cursor.executescript('''
CREATE VIEW IF NOT EXISTS india_yearly_summary AS
SELECT 
    year,
    SUM(india_exports) as total_exports,
    SUM(india_imports) as total_imports,
    SUM(india_trade_balance) as trade_balance,
    SUM(total_trade) as total_trade_volume
FROM trade_data
GROUP BY year
ORDER BY year;

CREATE VIEW IF NOT EXISTS top_trading_partners AS
SELECT 
    country,
    SUM(india_exports) as total_exports_to,
    SUM(india_imports) as total_imports_from,
    SUM(india_trade_balance) as total_trade_balance,
    SUM(total_trade) as total_trade_volume,
    COUNT(*) as years_of_data
FROM trade_data
GROUP BY country
ORDER BY total_trade_volume DESC;
''')

# Verify
cursor.execute("SELECT COUNT(*) FROM trade_data")
total_records = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(DISTINCT country) FROM trade_data")
unique_countries = cursor.fetchone()[0]

print(f"\nDatabase successfully created with:")
print(f"- {total_records:,} total trade records")
print(f"- {unique_countries} unique countries")
print(f"- Data from {df['Year'].min()} to {df['Year'].max()}")

# Sample queries to demonstrate
print("\nSample queries you can run:")
print("1. Get India's trade with China:")
print('   sqlite> SELECT * FROM trade_data WHERE country = "CHINA P RP" ORDER BY year;')

print("\n2. View India's yearly trade summary:")
print('   sqlite> SELECT * FROM india_yearly_summary;')

print("\n3. View top 10 trading partners:")
print('   sqlite> SELECT * FROM top_trading_partners LIMIT 10;')

print("\n4. Find countries with trade surplus with India:")
print('   sqlite> SELECT country, total_trade_balance FROM top_trading_partners WHERE total_trade_balance > 0 ORDER BY total_trade_balance DESC;')

# Close connection
conn.commit()
conn.close()

print("\nYou can now explore the database using:")
print(f"1. Command line: sqlite3 {db_path}")
print("2. DB Browser for SQLite (GUI tool)")
print("3. Python with sqlite3 module")
