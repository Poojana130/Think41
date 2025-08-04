import sqlite3
import pandas as pd

# Load CSVs
users = pd.read_csv("users.csv")
orders = pd.read_csv("orders.csv")

# Connect to SQLite DB
conn = sqlite3.connect("ecommerce.db")

# Write to tables
users.to_sql("users", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)

print("Data loaded successfully.")
