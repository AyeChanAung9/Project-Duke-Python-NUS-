dot_line = "-------------------------------------"
blank = " "


def intro():
    print("Hello! I'm Duke AKA (todo list Chat Bot)")
    print(blank)
    print(dot_line)
    print("I can do several Commands")
    avilable_commands()
    print("What can I do for you Today?")
    print(dot_line)
    print(blank)

def bye():
    print("---------------------------------")
    print("Bye. Hope to see you again soon!")

def avilable_commands():
    print(dot_line)
    print(blank)
    print("Available Commands are :")
    print(blank)
    print("---- todo ---- task ----")
    print("---- deadline ---- task ---- /by ---- due_time ----")

    print("---- event ---- task ---- /from -- start_time -- /to -- end_time ----")
    print("---- appointment ---- task ---- /from -- start_time -- /to -- end_time -- /at -- location ----")
    print("---- list ----")
    print("---- find ---- task ----")
    print("---- delete ---- task_number ----")
    print("---- mark ---- task_number ----")
    print("---- unmark ---- task ----")
    print("---- convert -- task_number -- /into -- task_type ----")
    print("---- export_as ---- (json or sqlite(default) ) ----")
    print("---- import ---- jsonfile(tasks.json) ----")
    print(blank)
    print(dot_line)


def store_format_print(file_format:str):
    print(dot_line)
    print(f"tasks are exported as {file_format} format")
    print(blank)

def tasks_imported_prompt():
    print(dot_line)
    print("Tasks are imported into the system")
    print(blank)

def close_line_prompt():
    print(blank)
    print(dot_line)
    print(blank)

def not_understand_prompt():
    print(dot_line)
    print("OOPS!!! I'm sorry, but I don't know what that means :(")
    close_line_prompt()

def task_not_found():
    print(dot_line)
    print("Task not found.")
    print(blank)

def description_cannot_be_empty(command:str):
    print(dot_line)
    print(f"OOPS!!! The description of a {command} cannot be empty")
    close_line_prompt()

def no_task_in_list():
    print(dot_line)
    print("There are no tasks in your list:")
    print(blank)

def search_task_not_found():
    print(dot_line)
    print("No matching task found in your list:")
    close_line_prompt()

def unsupported_task_format():
    print(dot_line)
    print("Task Description is an Unsupported Format.")
    print("Please follow Task Format.")
    close_line_prompt()

