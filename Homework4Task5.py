import sqlite3
import requests

url = 'https://api.monobank.ua/bank/currency'

response = requests.get(url)
con = sqlite3.connect('tableforHomework4Task5.db')
cursor = con.cursor()

data = response.json()
cur_hub = {
    840: 'UAH',
    980: 'EUR',
    124: 'GBP',
    191: 'JPY',
    208: 'CHF'
}
def currency_to_usd():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS mono (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   currency_name TEXT,
                   currency_value INTENGER,
                   current_date TEXT
                   )
                   ''')
    con.commit()

currency_to_usd()



def create_currency_to_usd(country):
    country = int(country)
    for item in data:
        if item["currencyCodeA"] == country and item["currencyCodeA"] == 840:
            print(item['rateBuy'])
            if country in cur_hub.keys():
                nazva = cur_hub[country]
                cursor.execute("INSERT INTO mono (currency_name, currency_value, current_date) VALUES (?, ?,?)",
                                (nazva, item["rateSell"], item["date"]))
                print(f'Курс {nazva} до USA успішно доданий в таблицю')
                con.commit()

def get_all_currency():
    cursor.execute("SELECT * FROM mono")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

while True:
    print('Hello to currency hub to usd'
            'please enter:'
            '840 to UAH'
            '980 to EUR'
            '124 to GBP'
            '191 to JPY'
            '208 to CHF'
            'q-to quit')
    choice = input('Enter your choice: ')
    if choice not in ['840','980','124','191','208','q']:
        print('Invalid choice, please try again')
        continue
    elif choice == 'q':
        break
    else:
        create_currency_to_usd(choice)
        get_all_currency()
        break


