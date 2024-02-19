from typing import Any
from database import task_store
from view import variables
from logic_model import logic

task_list: list[dict[str,Any]] = task_store.tasks_storage

def action_after_intro():
    task_store.load_tasks(variables.store_type)
    
def action_before_bye():
    task_store.save_tasks(variables.store_type)

def change_storing_format(file_format:str): # for switching persistence
    variables.store_type = file_format

#Return layer

def list_of_tasks():
    
    tasks_print: list[str] = []
    format_mapping = {
        variables.Todo: "{number}.   {type}  [{status}] {title}",
        variables.Deadline: "{number}.   {type}  [{status}] {title} (by: {due_time})",
        variables.Event: "{number}.   {type}  [{status}] {title} (from: {start_time} to: {end_time})",
        variables.Appointment: "{number}.   {type}  [{status}] {title} (from: {start_time} to: {end_time}) at: {location}"
    }
    if len(task_list) > 0:
        number = 1
        for task in task_list:
            status = variables.mark_symbol if task ["done"] else " "
            task_type = task ["type"] if isinstance(task ['type'], str) else ""

            format_string = format_mapping [task_type] 

            if format_string:
                ready_task = (format_string.format(
                    number = number,
                    type = task["type"],
                    status = status,
                    title = task["title"],
                    due_time = task.get("due_time", ""),
                    start_time = task.get("start_time", ""),
                    end_time = task.get("end_time", ""),
                    location = task.get("location", "")
                ))
                tasks_print.append(ready_task)
            number += 1
    return tasks_print

def find_task(keyword: str):
    match_task: list[str]= []
    for task in task_list:
        if isinstance(task ['title'], str) and keyword in task ['title']:
            no = 1
            status = variables.mark_symbol if task ["done"] else " "
            task_type = task ["type"]
            title = task ["title"]
            info_of_task = ''

            if task_type == variables.Todo:
                info_of_task = (f" {title} ")
            elif task_type == variables.Deadline:
                due_time = task ["due_time"]
                info_of_task = (f" {title} (by: {due_time})")
            elif task_type == variables.Event:
                start_time = task ["start_time"]
                end_time = task ["end_time"]
                info_of_task = (f" {title} (from: {start_time} to: {end_time})")
            elif task_type == variables.Appointment:
                start_time = task ["start_time"]
                end_time = task ["end_time"]
                location = task ["location"]
                info_of_task = (f" {title} (from: {start_time} to: {end_time}) at: {location}")


            found_task = f"{no}.   {task_type}[{status}] {info_of_task} "
            match_task.append(found_task)
            no += 1
    return match_task

def convert_task(command: str):
    command_split = command.split(" /into ") # spliting command to convert task type
    if len(command_split) != 2:
        return None
    index = command_split [0]
    task_type = command_split [1]
    task_index = int(index) - 1

    if 0 <= task_index <= len (task_list):
        logic.convert(task_list,task_index, task_type)
        return "converted"
    else:
        return None


def delete_task(index: str):
    task_index = int(index) - 1
    if 0 <= task_index <= len (task_list):
        target_task = task_list [task_index]  

        status = variables.mark_symbol if task_list [task_index] ["done"] else " "  # Preparing for output display
        task_type = target_task ["type"]
        title = target_task ["title"]
        info_of_task = ''

        if task_type == variables.Todo:
            info_of_task = (f" {title} ")
        elif task_type == variables.Deadline:
            due_time = target_task ["due_time"]
            info_of_task = (f" {title} (by: {due_time})")
        elif task_type == variables.Event:
            start_time = target_task  ["start_time"]
            end_time = target_task["end_time"]
            info_of_task = (f" {title} (from: {start_time} to: {end_time})")
        elif task_type == variables.Appointment:
            start_time = target_task ["start_time"]
            end_time = target_task ["end_time"]
            location = target_task ["location"]
            info_of_task = (f" {title} (from: {start_time} to: {end_time}) at: {location}")

        task_to_delete = f"    {task_type}[{status}] {info_of_task}"

        logic.delete(task_list,task_index)      # task deleting part

        return task_to_delete
    else:
        return None


def mark_task(index: str):
    task_index = int(index) - 1
    if 0 <= task_index <= len (task_list):
        logic.mark(task_list,task_index)        # task marking part

        target_task = task_list [task_index]         # Preparing for output display

        status = variables.mark_symbol if task_list [task_index] ["done"] else " "  
        task_type = target_task ["type"]
        title = target_task ["title"]
        info_of_task = ''

        if task_type == variables.Todo:
            info_of_task = (f" {title} ")
        elif task_type == variables.Deadline:
            due_time = target_task ["due_time"]
            info_of_task = (f" {title} (by: {due_time})")
        elif task_type == variables.Event:
            start_time = target_task ["start_time"]
            end_time = target_task ["end_time"]
            info_of_task = (f" {title} (from: {start_time} to: {end_time})")
        elif task_type == variables.Appointment:
            start_time = target_task ["start_time"]
            end_time = target_task ["end_time"]
            location = target_task ["location"]
            info_of_task = (f" {title} (from: {start_time} to: {end_time}) at: {location}")

        mark_target_task = f"    {task_type}[{status}] {info_of_task}"

        return mark_target_task
    else:
        return None


def unmark_task(index: str):
    task_index = int(index) - 1
    if 0 <= task_index <= len (task_list):
        logic.unmark(task_list,task_index)      # task unmarking part

        target_task = task_list [task_index]     # Preparing for output display
        
        status = variables.mark_symbol if task_list [task_index]["done"] else " "
        task_type = target_task ["type"]
        title = target_task ["title"]
        info_of_task = ''

        if task_type == variables.Todo:
            info_of_task = (f" {title} ")
        elif task_type == variables.Deadline:
            due_time = target_task ["due_time"]
            info_of_task = (f" {title} (by: {due_time})")
        elif task_type == variables.Event:
            start_time = target_task ["start_time"]
            end_time = target_task ["end_time"]
            info_of_task = (f" {title} (from: {start_time} to: {end_time})")
        elif task_type == variables.Appointment:
            start_time = target_task ["start_time"]
            end_time = target_task ["end_time"]
            location = target_task ["location"]
            info_of_task = (f" {title} (from: {start_time} to: {end_time}) at: {location}")

        mark_target_task = f"    {task_type}[{status}] {info_of_task}"

        return mark_target_task
    else:
        return None


def import_json_tasks(filename:str):
    logic.importer(task_list,filename)


def handle_todo(task_info: str):    
    task_id = len (task_list) 
    task_type = variables.Todo
    logic.add_task(task_list,task_id,task_type,task_info) 
    
    return (task_id + 1,task_info)  #returning output materials


def handle_deadline(task_info: str):
    task_split = task_info.split(" /by ") # spliting task to add task
    if len(task_split) != 2:
        return None
    
    info_of_task =task_split[0]
    due_time =task_split[1]

    task_type = variables.Deadline
    task_id = len(task_list)
    logic.add_task(task_list,task_id,task_type,info_of_task,due_time=due_time)
    
    return (task_id + 1, info_of_task, due_time)    #returning output materials  
   

def handle_event(task_info: str):
    task_split = task_info.split(" /from ") # spliting task to add task
    if len(task_split) != 2:
        return None
    info_of_task =task_split[0]

    time = task_split[1].split("/to")
    if len(time) != 2:
        return None
    
    start_time = time[0]
    end_time = time[1]

    task_id = len(task_list)    
    task_type = variables.Event
    logic.add_task(task_list,task_id,task_type,info_of_task,start_time=start_time,end_time=end_time)
    
    return (task_id + 1, info_of_task, start_time, end_time)    #returning output materials


def handle_appointment(task_info: str):
    task_split = task_info.split(" /from ") # spliting task to add task
    if len(task_split) != 2:
        return None
    info_of_task =task_split[0]

    time = task_split[1].split("/to")
    if len(time) != 2:
        return None
    
    start_time = time[0]
    appoint = time[1].split("/at")
    if len(appoint) != 2:
        return None
    end_time = appoint[0]
    location = appoint[1]

    task_id = len(task_list)    
    task_type = variables.Appointment
    logic.add_task(task_list,task_id, task_type, info_of_task, start_time=start_time, end_time=end_time, location=location)
    
    return (task_id + 1, info_of_task, start_time, end_time,location) 



