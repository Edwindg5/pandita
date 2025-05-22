from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json
import os
import secrets

app = Flask(__name__, static_folder='static')
app.secret_key = secrets.token_hex(16)
DB_FILE = 'diario.json'

# Inicializar base de datos JSON
def init_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=2)

# Obtener todas las notas
def get_notes():
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        init_db()
        return []

# Añadir nueva nota
def add_note(title, content, reminder=None):
    notes = get_notes()
    notes.insert(0, {
        'id': secrets.token_hex(4),
        'title': title,
        'content': content,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'reminder': reminder
    })
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

# Rutas
@app.route('/')
def home():
    return render_template('index.html', notes=get_notes())

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title', '').strip()
    content = request.form.get('content', '').strip()
    reminder = request.form.get('reminder')
    
    if title and content:
        add_note(title, content, reminder if reminder else None)
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)