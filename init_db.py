import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

with open("schema.sql", "r") as file:
    sql_script = file.read()

cursor.executescript(sql_script)

cursor.execute(
    "INSERT INTO categories (name) VALUES (?)",
    ("Electronics",)
)

connection.commit()
connection.close()