[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/C3R1qTnj)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11604934&assignment_repo_type=AssignmentRepo)
# proj-duke

Project Duke is an educational software project designed to take you through the steps of building a small software incrementally, while applying software engineering techniques as possible along the way.

The project aims to build a product named Duke, a Personal Assistant Chatbot that helps a person to keep track of various things. The name Duke was chosen as a placeholder name, in honor of Duke, the Java Mascot, which is the language used in the SE textbook. We will instead be using Python.

## User Guide (Sample Interaction with Duke)
> ```
> Hello! I'm Duke AKA (todo list Chat Bot)
> 
>-------------------------------------
>I can do several Commands
>-------------------------------------
> 
>Available Commands are :
> 
>---- todo ---- task ----
>---- deadline ---- task ---- /by ---- due_time ----
>---- event ---- task ---- /from -- start_time -- /to -- end_time ----
>---- appointment ---- task ---- /from -- start_time -- /to -- end_time -- /at -- location ----
>---- list ----
>---- find ---- task ----
>---- delete ---- task_number ----
>---- mark ---- task_number ----
>---- unmark ---- task ----
>---- convert -- task_number -- /into -- task_type ----
>---- export_as ---- (json or sqlite(default) ) ----
>---- import ---- jsonfile(tasks.json) ----
> 
>-------------------------------------
>What can I do for you Today?
>-------------------------------------
>
> > todo borrow book
> ---------------------------------
> Got it. I've added this task:
>   todo [ ] borrow book
> Now you have 1 tasks in the list.
>
> ---------------------------------
>
> > deadline return book /by Sunday
> ---------------------------------
> Got it. I've added this task:
>   deadline [ ] return book (by: Sunday)
> Now you have 2 tasks in the list.
>
> ---------------------------------
>
> > event project meeting /from Mon 2pm /to 4pm
> ---------------------------------
> Got it. I've added this task:
>   event [ ] project meeting (from: Mon 2pm to: 4pm)
> Now you have 3 tasks in the list.
>
> ---------------------------------
>
> > appointment presentation /from Mon 2pm /to 4pm /at University
> ---------------------------------
> Got it. I've added this task:
>   appointment [ ] presentation (from: Mon 2pm to: 4pm) at University
> Now you have 4 tasks in the list.
>
> ---------------------------------
> > list
> ---------------------------------
> Here are the tasks in your list:
> 1.  todo [ ] borrow book
> 2.  deadline [ ] return book (by: Sunday)
> 3.  event [ ] project meeting (from: Mon 2pm to: 4pm)
> 4.  appointment [ ] presentation (from: Mon 2pm to: 4pm) at University
>
> ---------------------------------
>
> > mark 1
> ---------------------------------
> Nice! I've marked this task as done:
>   todo [X] borrow book
>
> ---------------------------------
>
> > unmark 1
> ---------------------------------
> OK, I've marked this task as not done yet:
>   todo [ ] borrow book
>
> ---------------------------------
>
> > find book
> ---------------------------------
> Here are the matching tasks in your list:
>   todo [ ] borrow book
>   deadline [ ] return book (by: Sunday)
>
> ---------------------------------
>
> > delete 2
> ---------------------------------
> Noted. I've removed this task:
>   deadline [ ] return book (by: Sunday)
> Now you have 2 tasks in the list.
>
> ---------------------------------
>
> > list
> ---------------------------------
> Here are the tasks in your list:
> 1.  todo [ ] borrow book
> 2.  event [ ] project meeting (from: Mon 2pm to: 4pm)
> 3.  appointment [ ] presentation (from: Mon 2pm to: 4pm) at University
>
> ---------------------------------
>
> > blah
> ---------------------------------
> OOPS!!! I'm sorry, but I don't know what that means :(
>
> ---------------------------------
>
> convert 2 /into todo
>-------------------------------------
>Noted. I've converted this task:
>-------------------------------------
>
> > list
> ---------------------------------
> Here are the tasks in your list:
> 1.  todo [ ] borrow book
> 2.  todo [ ] project meeting
> 3.  appointment [ ] presentation (from: Mon 2pm to: 4pm) at University
>
> ---------------------------------
> export_as sqlite
>-------------------------------------
>tasks are exported as sqlite format
>
> ---------------------------------
> import tasks.json
>-------------------------------------
>Tasks are imported into the system
>
> todo
> ---------------------------------
> OOPS!!! The description of a todo cannot be empty
>
> ---------------------------------
>
> > bye
> ---------------------------------
> Bye. Hope to see you again soon!
> ```

## Types of Tasks

There are three types of tasks:
1. Todos: tasks without any date/time attached to it e.g., visit new theme park
2. Deadlines: tasks that need to be done before a specific date/time e.g., *submit report by 11/10/2019 5pm*
3. Events: tasks that start at a specific date/time and ends at a specific date/time
4. Appointment: tasks that start at a specific date/time and ends at a specific date/time at a specific location
e.g., (a) *team project meeting 2/10/2019 2-4pm (b) orientation week 4/10/2019 to 11/10/2019*

For now, date/time can be treated as a string.

## Other Commands
Tasks can be marked as done using the command `mark` and unmarked using `unmark`.
They can also be deleted with the `delete` command.
Tasks can be converted into another task type by using `convert` command.
All the tasks can be export as json or sqlite(default) using `export_as` command.
External Tasks in json format can be imported into the system using `import` command.

The command `find` give users a way to find a task by searching for a keyword. `list` simply lists all tasks.

## Persistency

Save the tasks in the hard disk automatically after the command `bye` all the task manipulation in chat bot will be save into sqlite database file (by default)
if u want to save as json file format chatbot also support with the command `export_as`.
Load the data from the hard disk when the chatbot starts up. 


## Components Explanation 

## duke-cli

duke-cli act as a command center for accepting command given from the cli.
duke-cli follow command pattern.
When the command come from duke-cli check valid or not route each command to respective function.

## View_handler

view_handler handle everything that need to be display to the user.
keep display materials and logic model seperate.

## Prompt and variables

Prompt store all the prompt that need to display as functions and can be used by view_handler when necessary
variables store variables that need to be use several time so that when we want to change something we just need to change variable value and not modify each functions

## Logic_model

Logic_model include 2 parts 
logic which do all the necessary manipulation to tha data (`add_task`,`delete`,`mark`,`unmark`,`convert`,`import`)
action_functions which return materials that need to be display for user to the view_handler(aka view layer)

## task_store

task_store act as a connecter between (database or file) and software
it include loading functions for json format and sqlite format to the software and saving functions to both.
Future extension for different file formats can be done in this. 

## duke-web

dukeweb connect with api to sent and receive materials
it act as converter between GUI interface and backend components.
it reuse functions form action_functions' logic layer so that both GUI and CLI use same logic model.

## Connection between components
Connections between each components can be seen architecture and class diagrams

## Future extensions
Future extensions can be done easily in each components without the need of modifying existing.
Example : different type of saving type (txt,databases)
          new feature adding
          new tasks adding
