from view import variables
import json
import sqlite3
from typing import Any

tasks_storage: list[dict[str, Any]] = []     #tasks storage for loaded tasks and manipulation tasks

#Central storage Manager

def save_tasks(store_format:str):
    if store_format == variables.json:
        __save_tasks_json()
    elif store_format == variables.sqlite:
        __save_tasks_sqlite()

def load_tasks(store_format:str):
    if store_format == variables.json:
        load_tasks_json(variables.FileName)
    elif store_format == variables.sqlite:
        __load_tasks_sqlite()


#json format

def __save_tasks_json():
    with open(variables.FileName, 'w') as file:
        json.dump(tasks_storage, file)

def load_tasks_json(filename:str)-> list[dict[str, Any]]:
    try:
        with open(filename, 'r') as file:
            loaded_data = json.load(file)
            if not isinstance(loaded_data, list):
                return []
            tasks_storage.extend(loaded_data)
            
    except FileNotFoundError:
        return []


#sqlite format

def __save_tasks_sqlite():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute('DELETE FROM tasks')

    for task in tasks_storage:
        c.execute('INSERT INTO tasks (id,done, type, title, due_time, start_time, end_time, location) VALUES (? ,?, ?, ?, ?, ?, ?, ?)',
                  (task.get('id',''),str(task.get('done', '')), task.get('type', ''), task.get('title', ''),
                   task.get('due_time', ''), task.get('start_time', ''), task.get('end_time', ''), task.get('location', '') ))

    conn.commit()
    conn.close()


def __load_tasks_sqlite():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER,
             done TEXT,
             type TEXT,
             title TEXT,
             due_time TEXT,
             start_time TEXT,
             end_time TEXT,
             location TEXT)''')

    conn.commit()

    c.execute('SELECT * FROM tasks')
    loaded_data = c.fetchall()

    conn.close()

    for row in loaded_data:
        task = [{'id': row[0], 'done': row[1] == 'True', 'type': row[2], 'title': row[3],
                        'due_time': row[4], 'start_time': row[5], 'end_time': row[6], 'location': row[7]}]
        tasks_storage.extend(task)
        
             