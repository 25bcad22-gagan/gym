from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Create DB
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            plan TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Add member
@app.route('/add_member', methods=['POST'])
def add_member():
    data = request.json

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO members (name, age, plan) VALUES (?, ?, ?)",
                   (data['name'], data['age'], data['plan']))

    conn.commit()
    conn.close()

    return jsonify({"message": "Member added successfully"})

# Get all members
@app.route('/get_members', methods=['GET'])
def get_members():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM members")
    rows = cursor.fetchall()

    conn.close()

    members = []
    for row in rows:
        members.append({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "plan": row[3]
        })

    return jsonify(members)

if __name__ == '__main__':
    app.run(debug=True)