import os
from dotenv import load_dotenv
import psycopg

load_dotenv()

try:
    connection = psycopg.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=int(os.getenv("DB_PORT")),
        sslmode="require"
    )

    cursor = connection.cursor()

    # Execute schema.sql
    with open("schema.sql", "r") as file:
        cursor.execute(file.read())

    # Insert categories
    cursor.execute("""
        INSERT INTO categories (name)
        VALUES
        ('Electronics'),
        ('Furniture'),
        ('Kitchen')
        ON CONFLICT (name) DO NOTHING;
    """)

    # Insert locations
    cursor.execute("""
        INSERT INTO locations (name)
        VALUES
        ('Bedroom'),
        ('Kitchen'),
        ('Living Room')
        ON CONFLICT (name) DO NOTHING;
    """)

    connection.commit()
    print("Database initialized successfully!")

except Exception as e:
    print("Error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()