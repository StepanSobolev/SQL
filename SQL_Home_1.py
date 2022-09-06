import os
import sqlite3

path = os.path.join(os.getcwd(), 'chinook.db')
con = sqlite3.Connection(path)


def get_first_name(con):
    last_name = con.execute('SELECT FirstName FROM customers').fetchall()
    last_name_list = []
    for name in last_name:
        ron = ''
        last_name_list.append(ron.join(name))
    return last_name_list


def show_people(people):
    for name in people:
        print(f'{name} in table {people.count(name)} occurrences')

show_people(get_first_name(con))

