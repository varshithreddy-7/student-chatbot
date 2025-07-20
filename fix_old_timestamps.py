import sqlite3
import datetime

conn = sqlite3.connect("chatbot.db")
cursor = conn.cursor()

# Get all rows where timestamp is NULL
cursor.execute("SELECT id FROM messages WHERE timestamp IS NULL")
rows = cursor.fetchall()

# Update each row with current timestamp
for row in rows:
    id = row[0]
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("UPDATE messages SET timestamp = ? WHERE id = ?", (now, id))

conn.commit()
conn.close()
print("Old rows updated with current timestamp.")
