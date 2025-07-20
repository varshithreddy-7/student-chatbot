import sqlite3

conn = sqlite3.connect("chatbot.db")

# Add timestamp column without default
try:
    conn.execute("ALTER TABLE messages ADD COLUMN timestamp TEXT")
    print("Timestamp column added successfully.")
except sqlite3.OperationalError as e:
    print("Column might already exist:", e)

conn.commit()
conn.close()
