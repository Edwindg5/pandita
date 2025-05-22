from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
import json
import os
import secrets
from functools import wraps

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(16))

# Configuración
DB_FILE = '/tmp/diario.json' if os.environ.get('VERCEL') else 'diario.json'

# Helpers
def get_month_name(month_num):
    months = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    return months[int(month_num) - 1]

def init_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=2)

def get_notes():
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            notes = json.load(f)
            # Añadir información de estado para las tareas
            for note in notes:
                if note.get('is_task') and 'due_date' in note:
                    due_date = datetime.strptime(note['due_date'], '%Y-%m-%d')
                    note['is_overdue'] = due_date < datetime.now() and not note.get('completed', False)
            return notes
    except (FileNotFoundError, json.JSONDecodeError):
        init_db()
        return []

def save_notes(notes):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

# Rutas
@app.route('/')
def home():
    notes = get_notes()
    return render_template('index.html', notes=notes, get_month_name=get_month_name)

@app.route('/add', methods=['POST'])
def add_entry():
    title = request.form.get('title', '').strip()
    content = request.form.get('content', '').strip()
    reminder = request.form.get('reminder')
    
    if title and content:
        notes = get_notes()
        notes.insert(0, {
            'id': secrets.token_hex(4),
            'title': title,
            'content': content,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'reminder': reminder,
            'type': 'entry'
        })
        save_notes(notes)
    
    return redirect(url_for('home'))

@app.route('/add-event', methods=['POST'])
def add_event():
    title = request.form.get('title', '').strip()
    content = request.form.get('content', '').strip()
    date = request.form.get('date')
    time = request.form.get('time')
    
    if title and content and date and time:
        notes = get_notes()
        notes.insert(0, {
            'id': secrets.token_hex(4),
            'title': title,
            'content': content,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'event_date': date,
            'event_time': time,
            'is_event': True,
            'type': 'event'
        })
        save_notes(notes)
    
    return redirect(url_for('home'))

@app.route('/add-task', methods=['POST'])
def add_task():
    title = request.form.get('title', '').strip()
    content = request.form.get('content', '').strip()
    due_date = request.form.get('due_date')
    
    if title and content and due_date:
        notes = get_notes()
        notes.insert(0, {
            'id': secrets.token_hex(4),
            'title': title,
            'content': content,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'due_date': due_date,
            'completed': False,
            'is_task': True,
            'type': 'task'
        })
        save_notes(notes)
    
    return redirect(url_for('home'))

@app.route('/complete-task/<task_id>', methods=['POST'])
def complete_task(task_id):
    notes = get_notes()
    for note in notes:
        if note.get('id') == task_id and note.get('is_task'):
            note['completed'] = not note.get('completed', False)
            break
    save_notes(notes)
    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

app = app  # Para Vercel