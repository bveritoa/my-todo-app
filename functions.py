FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

# to see the docstrings
# print(help(get_todos))


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items in the text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())

# if you use this if it will run only here and now in
# app1 where is called later

