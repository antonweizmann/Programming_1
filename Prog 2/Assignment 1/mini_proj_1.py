#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
def my_input(expected_type: int, msg):
    """Makes sure the correct variable type is input
     :param expected_type: The type of variable expected for this input. 0 means integer and 1 means string.
     :param msg: The message the users is show with the input statement
     :return: the input variable of correct type
     """
    out = None
    while True:
        try:
            if expected_type == 0:
                out = int(input(msg))
            elif expected_type == 1:
                out = input(msg)
            else:
                print("Error: no known expected type specified", end="", file=sys.stderr)
            break
        except ValueError:
            if expected_type == 0:
                print("Error: expected input is an integer", file=sys.stderr)
    return out

def check_birthdate(date):
    if date[0] in range(1, 32) and date[1] in range(1, 13):
        return 0
    return 1


def add_entry(contacts: dict, name: str, phone: str, birthdate: tuple):
    """
    Add a new contact to the dictionary

    Parameters
    ----------
    contacts : dict
        Dictionary containing of the known contacts. The keys of the dictionary
        are str containing the name of the contact. The values are a list with
        a str containing the contact's phone number as the first element, and a tuple 
        containing the contact's birth date in the format (dd, mm) as second element.
    name : str
        Name of the new contact.
    phone : str
        Phone of the new contact.
    birthdate : tuple
        Birthdate of the new contact.

    Returns
    -------
    contacts : dict
        The updated dictionary after adding the new contact.

    """
    if check_birthdate(birthdate):
        print("Error: Birthdate not in correct format", file=sys.stderr)
        return contacts
    elif len(phone) != 9:
        print("Error: Phone-number not in correct format", file=sys.stderr)
        return contacts
    elif name in contacts:
        print("Error: Name is already registered", file=sys.stderr)
        return contacts
    contacts[name] = [phone, birthdate]
    return contacts


def change_entry(contacts: dict, name: str, new_phone: str):
    """
    DESCRIPTION

    Parameters
    ----------
    contacts : dict
        DESCRIPTION.
    name : str
        DESCRIPTION.
    new_phone : str
        DESCRIPTION.

    Returns
    -------
    contacts : TYPE
        DESCRIPTION.
    """
    if len(new_phone) != 9:
        print("Error: Phone number not in correct format", file=sys.stderr)
        return contacts
    elif not name in contacts:
        print("Error: Name not known", file=sys.stderr)
        return contacts
    contacts[name][0] = new_phone
    return contacts


def delete_entry(contacts: dict, name: str):
    if name in contacts:
        del contacts[name]
    print("Error: Name not known", file=sys.stderr)
    return contacts
    
def find_phone(contacts: dict, name: str):
    if name in contacts:
        return contacts[name][0]
    print("Error: Name not known", file=sys.stderr)
    return None

def list_all_names(contacts: dict):
    return list(contacts.keys())

def month_birthdays(contacts: dict, date: tuple):
    cur_month = date[1]
    birthdays = []
    for item in contacts.items():
        if item[1][1][1] == cur_month:
            birthdays.append((item[0], item[1][1][0]))
    return birthdays

def ask_input(text, options):
    usr_opt = 0
    while usr_opt == 0:
        print(text)
        for option in list(options.items()):
            print(option , end=" ")
        print("")
        usr_opt = parse_input(int(my_input(0, "")))
    return usr_opt

def parse_input(usr_opt):
    if usr_opt in range(1, 8):
        return usr_opt
    return 0
    
def main():
   
    options = {1: "Add entry", 2: "Change entry", 3: "Delete entry", 4: "Find phone",
               5: "Month birthdays", 6: "List names", 7: "Exit"}
    contacts = { }

    # Implement your code for main here..
    while True:
        usr_opt = ask_input("Please select on of the following options ", options)
        match usr_opt:
            case 1:
                name = input("Name: ")
                phone = input("Phone number: ")
                birthdate_day = int(my_input(0, "Birthdate day: "))
                birthdate_month = int(input("Birthdate month: "))
                birthdate = (birthdate_day, birthdate_month)
                contacts = add_entry(contacts, name, phone, birthdate)
            case 2:
                name = input("Name: ")
                new_phone = input("New phone number: ")
                contacts = change_entry(contacts, name, new_phone)
            case 3:
                name = input("Name: ")
                contacts = delete_entry(contacts, name)
            case 4:
                name = input("Name: ")
                print(find_phone(contacts, name))
            case 5:
                date_month = int(my_input(0, "Date month: "))
                date = (1, date_month)
                print(month_birthdays(contacts, date))
            case 6:
                print(list_all_names(contacts))
            case 7:
                exit()

# The main body of your program should only call the main() function like this:
if __name__=="__main__":    
    main()
    
    
