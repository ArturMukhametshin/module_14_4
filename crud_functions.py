import sqlite3

def initiate_db():
    connection = sqlite3.connect('shop.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER
    )
    ''')

    #for i in range(4):
        #cursor.execute('INSERT INTO Products ( title,'
                    #' description, price) VALUES (?, ?, ?)',
                #(f'Продукт {i + 1}', f'Описание {i + 1}', f'{(i + 1) * 10} руб.'))

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('shop.db')
    cursor = connection.cursor()

    cursor.execute("SELECT title, description, price FROM Products")
    users = cursor.fetchall()

    connection.commit()
    connection.close()
    return users

initiate_db()