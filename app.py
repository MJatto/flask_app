from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'data.db')

def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        with open(os.path.join(os.path.dirname(__file__), 'init_db.sql'), 'r') as f:
            conn.executescript(f.read())
        conn.close()

def get_messages():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM messages")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]

@app.route("/")
def home():
    init_db()
    messages = get_messages()
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)
