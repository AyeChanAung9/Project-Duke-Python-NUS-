from flask import Flask, send_from_directory, request
from typing import Any
from database import task_store
from logic_model import logic
from view import variables


app = Flask(__name__, static_url_path='', static_folder='assets/client')

task_store.load_tasks(variables.store_type)
task_list:list[dict[str,Any]] = task_store.tasks_storage

@app.get('/tasks')
def list_or_find():
    
    keyword = request.args['find']
    
    if keyword != "":
        found_list:list[dict[str,Any]]  = []
        for task in task_list:
            if keyword in task['title']:
                found_list.append(task)
        return found_list

    return task_list

@app.post('/tasks')
def create():
    factory = {'todo':todo , 'deadline':deadline , 'event':event}
    data :dict[str,Any]  = request.json
    type_of_task = data['type']
    payload = data['payload']

    if type_of_task in factory:
        factory[type_of_task](payload)
        return 'Task created successfully'
    else:
        return 'Invalid task type',400

@app.get('/')
def serve_client():
    return send_from_directory('assets/client', 'index.html')



@app.patch('/tasks/<int:id>/mark')
def mark(id: int):
    logic.mark(task_list,id)
    task_store.save_tasks(variables.store_type)
    return ''


@app.patch('/tasks/<int:id>/unmark')
def unmark(id: int):
    logic.unmark(task_list,id)
    task_store.save_tasks(variables.store_type)
    return ''


@app.delete('/tasks/<int:id>')
def delete(id: int):
    logic.delete(task_list,id)
    task_store.save_tasks(variables.store_type)
    return ''



def todo(payload:dict[str,str]):
    id = len(task_list)
    title = payload["title"]
    logic.add_task(task_list,id,"todo",title)
    task_store.save_tasks(variables.store_type)
    
def deadline(payload:dict[str,str]):
    id = len(task_list)
    title, due_time = payload.values()
    logic.add_task(task_list,id,"deadline",title,due_time=due_time)      
    task_store.save_tasks(variables.store_type)

def event(payload:dict[str,str]):
    id = len(task_list)
    title, start_time, end_time = payload.values()
    logic.add_task(task_list,id,"event",title,start_time=start_time,end_time=end_time)
    task_store.save_tasks(variables.store_type)

