import sqlite3
from uuid import uuid4

db = sqlite3.connect('DB/bots.sqlite3')
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS bots(
    id INT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    author TEXT NOT NULL,
    prefix TEXT NOT NULL,
    token TEXT
)""")

class BotAdd():
    """This function creates a new bot and adds it to the database"""
    def __init__(self, name, author, prefix):
        """Initializing function"""
        self.name = name
        self.author = author
        self.prefix = prefix
        token = str(uuid4())
        rows_count = cursor.execute("SELECT COUNT() FROM bots").fetchone()[0]

        if rows_count == 0:
            last_id = 0
        else:
            last_id = cursor.execute(f"SELECT id FROM bots").fetchall()[-1:][0][0]


        cursor.execute("INSERT INTO bots VALUES(?, ?, ?, ?, ?)", (last_id+1, self.name, self.author, self.prefix, token))
        db.commit()

        print(f'Бот создан\nИмя бота: {self.name}\nID: {last_id+1}\nАвтор бота: {self.author}\nПрефикс бота: {self.prefix}\nТокен бота: {token}')



# class Login():
#     def __init__(self, token):
#         """Initializing function"""
#
#         self.token = token
#
#         if cursor.execute(f"SELECT token FROM bots WHERE token = {self.token}").fetchone() is None:
#             print('Error! Token is invalid')
#         else:
#             print('Login success')


BotAdd('BorryBot', 'Oleg', '-')