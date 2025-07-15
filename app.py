from flask import Flask, render_template, request, g
from chatbot import get_bot_response
import sqlite3

app = Flask(__name__)
DATABASE = "chatbot.db"

# DB helpers
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

@app.route("/", methods=["GET", "POST"])
def home():
    db = get_db()
    if request.method == "POST":
        user_query = request.form["query"]
        bot_response = get_bot_response(user_query)

        # Save to database
        db.execute("INSERT INTO messages (user_message, bot_reply) VALUES (?, ?)", (user_query, bot_response))
        db.commit()

    # Fetch full chat history
    cur = db.execute("SELECT user_message, bot_reply FROM messages ORDER BY id ASC")
    chat_history = [{"user": row[0], "bot": row[1]} for row in cur.fetchall()]

    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
