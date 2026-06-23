from flask import Flask, render_template
import requests
import sqlite3

app = Flask(__name__)

# Create database
def init_db():

    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT,
            author TEXT
        )
    ''')

    conn.commit()
    conn.close()


@app.route('/')
def home():

    # Fetch quote from API
    response = requests.get("https://zenquotes.io/api/random")

    data = response.json()[0]

    quote = data['q']
    author = data['a']

    # Connect database
    conn = sqlite3.connect('quotes.db')
    cursor = conn.cursor()

    # Insert quote
    cursor.execute(
        "INSERT INTO quotes (quote, author) VALUES (?, ?)",
        (quote, author)
    )

    conn.commit()

    # Fetch history
    cursor.execute("SELECT * FROM quotes ORDER BY id DESC")

    history = cursor.fetchall()

    conn.close()

    return render_template(
        'index.html',
        quote=quote,
        author=author,
        history=history
    )


if __name__ == '__main__':

    init_db()

    app.run(debug=True)