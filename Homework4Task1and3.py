# Завдання 1
# Зробіть таблицю для підрахунку особистих витрат із такими полями: id, призначення, сума, час.
# Завдання 3
# Змініть таблицю так, щоби можна було додати не лише витрати, а й прибутки.

import sqlite3

con = sqlite3.connect('expenses.db')
cursor = con.cursor()

def wallet():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        spending,
        salary,
        sum_of_spend INTEGER,
        sum_of_salary INTEGER,
        time_of_deal TEXT NOT NULL
    )
    ''')
    con.commit()
wallet()

def add_expense(spending, sum_of_spend, time_of_deal):
    cursor.execute('''
    INSERT INTO expenses (spending, sum_of_spend, time_of_deal) VALUES (?, ?, ?)''', 
                   (spending, sum_of_spend, time_of_deal))
    print('Витрата успішно додана!')
    con.commit()

def add_salary(salary,sum_of_salary, time_of_deal):
    cursor.execute('''
                INSERT INTO expenses (salary,sum_of_salary, time_of_deal) VALUES (?, ?, ?)''', 
                (salary, sum_of_salary, time_of_deal))
    print('Зарплата успішно додана!')
    con.commit()




def get_total_spending():
    cursor.execute('SELECT SUM(sum_of_spend) FROM expenses')
    result = cursor.fetchone()
    return result[0] if result[0] is not None else 0

def get_total_salary():
    cursor.execute('SELECT SUM(sum_of_salary) FROM expenses')
    result = cursor.fetchone()
    return result[0] if result[0] is not None else 0


def get_all_expenses():
    cursor.execute('SELECT * FROM expenses')
    return cursor.fetchall()

def get_all_salary():
    cursor.execute('SELECT * FROM salary')
    return cursor.fetchall()



add_expense('Продукти', 300, '2024-12-12')
add_expense('Транспорт', 150, '2024-12-11')
add_expense('Кафе', 200, '2024-12-10')
add_salary('булка', 121, '2024-12-12')
add_salary('пельмень', 232, '2024-12-11')
add_salary('картошка', 3, '2024-12-09')
print('Всі витрати:')
for row in get_all_expenses():
    print(row)
for rowd in get_all_salary():
    print(rowd)

print('Загальна сума витрат:', get_total_spending())

print('Всі зарплати:', get_total_salary())


con.close()
