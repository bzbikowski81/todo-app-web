def get_todo_list(filepath="todo_list.txt"):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, "r") as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_todo_list(todo_list_arg, filepath="todo_list.txt"):
    """ Write the to-do items list in the text file. """
    with open(filepath, "w") as file:
        file.writelines(todo_list_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todo_list())