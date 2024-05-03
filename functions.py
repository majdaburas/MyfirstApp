import time
import pathlib


def get_todo():
    with open("todos.txt", "r") as local_file:
        local_todos = local_file.readlines()
    return local_todos


def get_todo_w(todos):
    with open("todos.txt", "w") as file:
        file.writelines(todos)


def completed_list():
    date = time.strftime("%d-%m-%Y")
    try:
        with open("days/" + date + ".txt", "r") as complete:
            completed_todos = complete.readlines()
        return completed_todos
    except FileNotFoundError:
        with open("days/" + date + ".txt", "w") as complete:
            with open("days/" + date + ".txt", "r") as complete:
                completed_todos = complete.readlines()
        return completed_todos


def save_completed(completed_todos):
    date = time.strftime("%d-%m-%Y")
    with open("days/" + date + ".txt", "w") as file:
        file.writelines(completed_todos)



def dates():
    folder = pathlib.Path("files")
    files = [file.name for file in folder.iterdir() if file.is_file()]
    return files