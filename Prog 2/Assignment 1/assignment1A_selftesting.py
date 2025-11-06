#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import the file with your solutions
import mini_proj_1 as asgmt


# Define different testing functions
def test_add_entry():
    """Tests adding two entries to an empty dictionary"""
    contacts = {}

    name = 'Name1'
    phone = '123456789'
    birthday = (22, 2)
    contacts = asgmt.add_entry(contacts, name, phone, birthday)

    name = 'Name2'
    phone = '234567890'
    birthday = (20, 12)
    contacts = asgmt.add_entry(contacts, name, phone, birthday)

    contacts_ = {'Name1': ['123456789', (22, 2)], 'Name2': [
        '234567890', (20, 12)]}
    if contacts == contacts_:
        print("Passed test_add_entry")
    else:
        print("Failed test_add_entry")

def test_add_same_entry():
    """Tests adding an entry that already exist to a contacts dictionary"""
    contacts = {'Name1': ['123456789', (10, 2)]}

    name = 'Name1'
    phone = '234567890'
    birthday = (10, 2)
    contacts = asgmt.add_entry(contacts, name, phone, birthday)

    contacts_ = {'Name1': ['123456789', (10, 2)]}
    if contacts == contacts_:
        print("Passed test_add_same_entry")
    else:
        print("Failed test_add_same_entry")

def test_add_invalid_phone_number():
    contacts = {'Name1': ['123456789', (10, 2)]}

    name = 'Name2'
    phone = '1234567890'
    birthday = (10, 2)
    contacts = asgmt.add_entry(contacts, name, phone, birthday)

    name = 'Name3'
    phone = '12345678'
    birthday = (10, 2)
    contacts = asgmt.add_entry(contacts, name, phone, birthday)

    contacts_ = {'Name1': ['123456789', (10, 2)]}
    if contacts == contacts_:
        print("Passed test_add_invalid_phone_number")
    else:
        print("Failed test_add_invalid_phone_number")


def test_add_invalid_date():
    contacts = {'Name1': ['123456789', (10, 2)]}

    name = 'Name2'
    phone = '123456789'
    birthday = (1, 13)
    contacts = asgmt.add_entry(contacts, name, phone, birthday)

    name = 'Name2'
    phone = '123456789'
    birthday = (1, 0)
    contacts = asgmt.add_entry(contacts, name, phone, birthday)

    name = 'Name3'
    phone = '123456789'
    birthday = (32, 1)
    contacts = asgmt.add_entry(contacts, name, phone, birthday)

    name = 'Name4'
    phone = '123456789'
    birthday = (0, 1)
    contacts = asgmt.add_entry(contacts, name, phone, birthday)

    contacts_ = {'Name1': ['123456789', (10, 2)]}
    if contacts == contacts_:
        print("Passed test_add_invalid_date")
    else:
        print("Failed test_add_invalid_date")


def test_change_entry():
    contacts = {'Name1': ['123456789', (10, 2)],
                'Name2': ['123456780', (11, 1)]}

    name = 'Name1'
    new_phone = '234567890'

    contacts = asgmt.change_entry(contacts, name, new_phone)
    contacts_ = {'Name1': ['234567890', (10, 2)],
          'Name2': ['123456780', (11, 1)]}
    if contacts == contacts_:
        print("Passed test_change_entry")
    else:
        print("Failed test_change_entry")

def test_change_invalid_name():
    contacts = {'Name1': ['123456789', (10, 2)],
                'Name2': ['123456780', (11, 1)]}

    name = 'Name3'
    new_phone = '234567890'

    contacts = asgmt.change_entry(contacts, name, new_phone)
    contacts_ = {'Name1': ['123456789', (10, 2)],
          'Name2': ['123456780', (11, 1)]}
    if contacts == contacts_:
        print("Passed test_change_invalid_name")
    else:
        print("Failed test_change_invalid_name")

def test_change_invalid_number():
    contacts = {'Name1': ['123456789', (10, 2)],
                'Name2': ['123456780', (11, 1)]}

    name = 'Name1'
    new_phone = '1234567890'

    contacts = asgmt.change_entry(contacts, name, new_phone)

    name = 'Name2'
    new_phone = '12345678'

    contacts = asgmt.change_entry(contacts, name, new_phone)

    contacts_ = {'Name1': ['123456789', (10, 2)],
          'Name2': ['123456780', (11, 1)]}
    if contacts == contacts_:
        print("Passed test_change_invalid_number")
    else:
        print("Failed test_change_invalid_number")


def test_delete_entry():
    contacts = {'Name1': ['123456789', (10, 2)],
                'Name2': ['123456780', (11, 1)]}

    name = 'Name2'
    contacts = asgmt.delete_entry(contacts, name)
    contacts_ = {'Name1': ['123456789', (10, 2)]}
    if contacts == contacts_:
        print("Passed test_delete_entry")
    else:
        print("Failed test_delete_entry")

def test_delete_invalid_name():
    contacts = {'Name1': ['123456789', (10, 2)],
                'Name2': ['123456780', (11, 1)]}
    name = 'Name3'

    contacts = asgmt.delete_entry(contacts, name)
    contacts_ = {'Name1': ['123456789', (10, 2)],
          'Name2': ['123456780', (11, 1)]}
    if contacts == contacts_:
        print("Passed test_delete_invalid_name")
    else:
        print("Failed test_delete_invalid_name")


def test_birthdays():

    contacts = {'Name1': ['123456789', (2, 4)],
                'Name2': ['223456789', (4, 2)],
                'Name3': ['323456789', (20, 2)],
                'Name4': ['423456789', (20, 2)]}

    date = (1, 2)
    bdays = asgmt.month_birthdays(contacts, date)
    bdays_ = [('Name2', 4),
              ('Name4', 20),
              ('Name3', 20),
              ]
    test = True
    for bday_ in bdays_:
        if bday_ not in bdays:
            test = False    
    if ('Name1', 2) in bdays:
        test = False
    if test:
        print("Passed test_birthdays")
    else:
        print("Failed test_birthdays")

        
def test_no_birthdays():

    contacts = {'Name1': ['123456789', (2, 4)],
                'Name2': ['223456789', (4, 2)],
                'Name3': ['323456789', (20, 2)],
                'Name4': ['423456789', (20, 2)]}

    date = (1, 3)
    bdays = asgmt.month_birthdays(contacts, date)
    
    if bdays == []:
        print("Passed test_no_birthdays")
    else:
        print("Failed test_no_birthdays")



def main():
    
    print("Testing add_entry() function")
    test_add_entry()
    test_add_same_entry()
    test_add_invalid_phone_number()
    test_add_invalid_date()
    print(".................................")

    print("Testing change_entry() function")
    test_change_entry()
    test_change_invalid_name()
    test_change_invalid_number()
    print(".................................")
    
    print("Testing delete_entry() function")
    test_delete_entry()
    test_delete_invalid_name()
    print(".................................")
    
    print("Testing month_birthdays() function")
    test_birthdays()
    test_no_birthdays()
    print(".................................")
    
    
if __name__ == "__main__":
    main()
