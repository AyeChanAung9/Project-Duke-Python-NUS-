from typing import Any
from view import variables
from database import task_store

#Logic Layer

def add_task(tasks:list[dict[str,Any]],id: int, task_type: str, task_info: str, due_time: str = None, start_time: str = None, end_time: str = None, location: str = None) -> None:

    task_data = {
        "id" : id,
        "done": False,
        "type": task_type,
        "title": task_info ,
        "due_time": '',
        "start_time": '',
        "end_time": '',
        "location": ''

         }

    if task_type == variables.Deadline:
        task_data["due_time"] = due_time
    elif task_type == variables.Event:
        task_data["start_time"] = start_time
        task_data["end_time"] = end_time
    elif task_type == variables.Appointment:
        task_data["start_time"] = start_time
        task_data["end_time"] = end_time
        task_data["location"] = location

    tasks.append(task_data)



def delete(tasks:list[dict[str,Any]],index: int):
    tasks.pop(index)
    for i in range(index,len(tasks)):
        tasks[i]['id'] = i

def mark(tasks:list[dict[str,Any]],index: int):
    tasks[index]["done"] = True

def unmark(tasks:list[dict[str,Any]],index: int):
    tasks[index]["done"] = False

def convert(tasks:list[dict[str,Any]],task_index: int, task_type: str):
    tasks [task_index] ['type'] = task_type

def importer(tasks:list[dict[str,Any]],filename:str):
     task_store.load_tasks_json(filename)
     id_count = 0
     for task in tasks:
          task ["id"] = id_count
          id_count += 1