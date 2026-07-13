import os
from dotenv import load_dotenv
import psycopg

load_dotenv()

connection = psycopg.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=int(os.getenv("DB_PORT")),
    sslmode="require"
)

cursor = connection.cursor()
print("Connected successfully!")