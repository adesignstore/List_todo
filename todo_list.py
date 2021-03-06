"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""
    list_item = raw_input("What would you like to add? ")
    my_list.append(list_item)

def view_list(my_list):
    """Print each item in the list."""
    
    for items in my_list:
        print items

    # print my_list
    # # "The view_list function has not yet been written"
def delete_item(my_list):
    deleted_item = a_list.pop(0)
    deleted_list.append(deleted_item)
    for items in a_list:
        print items
    for items in deleted_list:
        print items

def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Quit the program
    D. Delete first item from list
    >>> """

    while True:
        answer = raw_input(user_options)
        answer = answer.upper()
        # Collect input and include your if/elif/else statements here.
        if answer == "A":
            add_to_list(my_list)
            # print my_list
        elif answer == "B":
            view_list(my_list)
        elif answer == "D":
            delete_item(my_list)

        elif answer == "C":
            break
        else:
            print " What?" 

#-------------------------------------------------

a_list = []
deleted_list = []
display_main_menu(a_list)

