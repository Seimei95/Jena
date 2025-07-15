from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn

# Initialize the database
def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT, completed INTEGER)')
    conn.commit()
    conn.close()

# Routes
@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML file

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return jsonify([dict(task) for task in tasks])

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    text = data.get('text')
    if not text:
        return jsonify({'error': 'Task text is required'}), 400
    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (text, completed) VALUES (?, ?)', (text, 0))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task added successfully'}), 201

@app.route('/api/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    completed = data.get('completed')
    if completed is None:
        return jsonify({'error': 'Completed status is required'}), 400
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET completed = ? WHERE id = ?', (completed, id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task updated successfully'})

@app.route('/api/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)