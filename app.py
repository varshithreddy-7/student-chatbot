from flask import Flask, render_template, request, g
import sqlite3
import datetime

app = Flask(__name__)
DATABASE = "chatbot.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

# Chatbot response function
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "course" in user_input:
        return "You can choose from CSE, ECE, IT, and more!"
    elif "placement" in user_input:
        return "Our college offers great placement support with top companies."
    elif "fees" in user_input:
        return "The fees structure varies based on the course. Please visit the college website."
    elif "cgpa" in user_input:
        return "CGPA stands for Cumulative Grade Point Average. It plays a major role in placements and higher studies."
    elif "dsa" in user_input:
        return "To prepare for DSA: - Start with arrays, strings, linked lists - Then move to trees, stacks, queues, graphs - Use platforms like LeetCode, InterviewBit - Try to solve 2-3 problems daily"
    elif "resume" in user_input:
        return "For a great resume: - Keep it 1 page - Highlight projects and internships - Use clear formatting - Include GitHub/LinkedIn links - Tailor it for the role"
    elif "project" in user_input or "ideas" in user_input:
        return "Here are some good project ideas: - URL Shortener with analytics - AI Chatbot for students (this one!) - Expense Tracker - Resume Ranker with AI - E-commerce site with Flask/Django"
    elif "internship" in user_input or "intern" in user_input:
        return "For internship preparation: - Build 2-3 strong projects - Practice DSA regularly - Prepare resume - Apply early to programs like Google STEP, Microsoft, Amazon WoW, etc."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that yet. Try asking about internships, CGPA, resume, or DSA."



@app.route("/", methods=["GET", "POST"])
def home():
    db = get_db()
    if request.method == "POST":
        user_query = request.form["message"]
        bot_response = get_bot_response(user_query)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to database with timestamp
        db.execute("INSERT INTO messages (user_message, bot_reply, timestamp) VALUES (?, ?, ?)",
                   (user_query, bot_response, timestamp))
        db.commit()

    # Fetch full chat history
    cur = db.execute("SELECT user_message, bot_reply, timestamp FROM messages ORDER BY id ASC")
    chat_history = [{"user": row[0], "bot": row[1], "time": row[2]} for row in cur.fetchall()]

    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
