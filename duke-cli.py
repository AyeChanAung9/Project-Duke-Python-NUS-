from view import View_handler

def main():
    command_map = {
                    "list": View_handler.view_list,
                    "delete": View_handler.view_delete,
                    "mark": View_handler.view_mark,
                    "unmark": View_handler.view_unmark,
                    "find": View_handler.view_found_tasks,
                    "todo": View_handler.view_todo,
                    "deadline": View_handler.view_deadline,
                    "event": View_handler.view_event,
                    "appointment": View_handler.view_appointment,
                    "convert": View_handler.view_convert,
                    "export_as": View_handler.store_format_view,
                    "import" :View_handler.import_json_view
                    }

    while True:
        response = input("> ").split(maxsplit=1) # slice the words
        command = response[0]
        
        if command == "bye":
            View_handler.bye_view()
            break

        if command in command_map:
            if len(response) > 1:
                target_index = response[1]
                command_map[command](target_index) # type: ignore
            else:
                try:
                    command_map[command]()
                except:
                    View_handler.empty_description(command)
        else:
            View_handler.mistake_words()

                   
if __name__ == "__main__":
    View_handler.intro_view()
    main()