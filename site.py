import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Create a SQLite database and table
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              value INTEGER)''')
conn.commit()

@app.route('/')
def index():
    # Retrieve all items from the table
    #c.execute("SELECT * FROM users")
    items = {"name":"diego","value":1}
    
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    # Add a new item to the table
    name = request.form['name']
    value = int(request.form['value'])
    c.execute("INSERT INTO users (name, value) VALUES (?, ?)", (name, value))
    conn.commit()
    return redirect('/')

@app.route('/remove/<int:item_id>', methods=['POST'])
def remove(item_id):
    # Remove an item from the table
    c.execute("DELETE FROM users WHERE id=?", (item_id,))
    conn.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run()