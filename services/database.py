import sqlite3

connection = sqlite3.connect(
    "database/credits.db"
)

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        credits INTEGER NOT NULL
    )
""")

connection.commit()