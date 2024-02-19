from typing import Union
from view import variables
from view import Prompts
from logic_model import action_functions

def intro_view():
    Prompts.intro()
    action_functions.action_after_intro()

def bye_view():
    Prompts.bye()
    action_functions.action_before_bye()

def store_format_view(file_format: str):
    action_functions.change_storing_format(file_format)
    Prompts.store_format_print(file_format)

def mistake_words():
    Prompts.not_understand_prompt()

def empty_description(command: str):
    Prompts.description_cannot_be_empty(command)

def import_json_view(filename:str):
    action_functions.import_json_tasks(filename)
    Prompts.tasks_imported_prompt()

def view_list():
    current_task_list = action_functions.list_of_tasks()
    if len(current_task_list) > 0:
        print(Prompts.dot_line)
        print("Here are the tasks in your list:")
        for task in current_task_list:
            print(task)
        print(Prompts.blank)

    else:
        Prompts.no_task_in_list()

def view_found_tasks(keyword: str):
    match_tasks_found = action_functions.find_task(keyword)
    if len(match_tasks_found) > 0:
        print(Prompts.dot_line)
        print("Here are the matching tasks in your list:")
        for founded_task in match_tasks_found:
            print(founded_task)
        Prompts.close_line_prompt()
    else:
        Prompts.search_task_not_found()

def view_delete(index: str):
    task_to_delete = action_functions.delete_task(index)
    if task_to_delete is not None:
        print(Prompts.dot_line)
        print("Noted. I've removed this task:")
        print(task_to_delete)
        print(Prompts.blank)
    else:
        Prompts.task_not_found()


def view_convert(command: str):
    convert = action_functions.convert_task(command)
    if convert is not None:
        print(Prompts.dot_line)
        print(f"Noted. I've {convert} this task:")
        print(Prompts.blank)
    else:
        Prompts.task_not_found()


def view_mark(index: str):
    marked_task =action_functions.mark_task(index)
    if marked_task is not None:
        mark_complete_prompt('M',marked_task)
    else:
        Prompts.task_not_found()

def view_unmark(index: str):
    unmarked_task =action_functions.unmark_task(index)
    if unmarked_task is not None:
        mark_complete_prompt('U',unmarked_task)
    else:
        Prompts.task_not_found()

def mark_complete_prompt(mark_type: str,task: str):
    print(Prompts.dot_line)
    if mark_type == variables.mark:
        print("Nice! I've marked this task as done.")
        print(task)
    elif mark_type == variables.unmark:
        print("Nice! I've unmarked this task as done.")
        print(task)
    print(Prompts.blank)



def view_todo(task_info: str):
    task_count, info_of_task = action_functions.handle_todo(task_info)
    adding_complete_prompt(variables.Todo,task_count, info_of_task)
    Prompts.close_line_prompt()

def view_deadline(task_info: str):
    check_task_description = action_functions.handle_deadline(task_info)
    if check_task_description is not None:
        task_count, info_of_task, due_time = check_task_description
        adding_complete_prompt(variables.Deadline,task_count, info_of_task, due_time)
        Prompts.close_line_prompt()
    else:
        Prompts.unsupported_task_format()

def view_event(task_info: str):
    check_task_description = action_functions.handle_event(task_info)
    if check_task_description is not None:
        task_count, info_of_task, start_time, end_time = check_task_description
        adding_complete_prompt(variables.Event,task_count, info_of_task, start_time, end_time)
        Prompts.close_line_prompt()
    else:
        Prompts.unsupported_task_format()

def view_appointment(task_info: str):
    check_task_description = action_functions.handle_appointment(task_info)
    if check_task_description is not None:
        task_count, info_of_task, start_time, end_time, location = check_task_description
        adding_complete_prompt(variables.Appointment,task_count, info_of_task, start_time, end_time, location)
        Prompts.close_line_prompt()
    else:
        Prompts.unsupported_task_format()

def adding_complete_prompt(task_type: str, *info:Union[int, str]):
    print(Prompts.dot_line)
    print("Got it.I've added this task:")
    if task_type == variables.Todo:
        print(f"    {variables.Todo}[ ] {info[1]}")
    elif task_type == variables.Deadline:
        print(f"    {variables.Deadline}[ ] {info[1]} (by: {info[2]})")
    elif task_type == variables.Event:
        print(f"    {variables.Event}[ ] {info[1]} (from: {info[2]} to: {info[3]})")
    elif task_type == variables.Appointment:
        print(f"    {variables.Appointment}[ ] {info[1]} (from: {info[2]} to: {info[3]})  at: {info[4]}")  
    print(f"Now you have {info[0]} tasks in the list.")








