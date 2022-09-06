import os
import sqlite3

path = os.path.join(os.getcwd(), 'chinook.db')
con = sqlite3.Connection(path)


def get_unitprice(con):
    unitprice = con.execute('SELECT UnitPrice FROM invoice_items').fetchall()
    unitprice_list = []
    for price in unitprice:
        num = float(''.join(map(str, price)))
        unitprice_list.append(num)
    return unitprice_list


def get_quantity(con):
    quantity = con.execute('SELECT Quantity FROM invoice_items').fetchall()
    quantity_list = []
    for i in quantity:
        num = float(''.join(map(str, i)))
        quantity_list.append(num)
    return quantity_list


unitprice = get_unitprice(con)
quantity = get_quantity(con)


def sum_order(unitprice, quantity):
    all_sum = 0
    for i in range(0, len(unitprice)):
        multiplication = unitprice[i] * quantity[i]
        all_sum += multiplication
    return all_sum


all_sum = sum_order(unitprice, quantity)
print(all_sum)
