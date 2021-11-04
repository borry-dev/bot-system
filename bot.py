import sqlite3
from uuid import uuid4

db = sqlite3.connect('DB/bots.sqlite3')
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS bots(
    id INT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    owner TEXT NOT NULL,
    prefix TEXT NOT NULL,
    token TEXT NOT NULL
)""")

class BotAdd():
    """This function creates a new bot and adds it to the database"""
    def __init__(self, name, owner, prefix):
        """Initializing function"""
        self.name = name
        self.owner = owner
        self.prefix = prefix
        token = str(uuid4())
        rows_count = cursor.execute("SELECT COUNT() FROM bots").fetchone()[0]

        if rows_count == 0:
            last_id = 0
        else:
            last_id = cursor.execute(f"SELECT id FROM bots").fetchall()[-1:][0][0]


        cursor.execute("INSERT INTO bots VALUES(?, ?, ?, ?, ?)", (last_id+1, self.name, self.owner, self.prefix, token))
        db.commit()

        print(f'Бот создан\nИмя бота: {self.name}\nID: {last_id+1}\nАвтор бота: {self.owner}\nПрефикс бота: {self.prefix}\nТокен бота: {token}')



class Login():
    def __init__(self, token):
        """Initializing function"""

        self.token = token


        if cursor.execute("SELECT token FROM bots WHERE token = (?)", (self.token,)).fetchone() is None:
            print('Error! Token is invalid')
        else:
            id = cursor.execute("SELECT id FROM bots WHERE token = (?)", (self.token,)).fetchone()[0]
            name = cursor.execute("SELECT name FROM bots WHERE token = (?)", (self.token,)).fetchone()[0]
            owner = cursor.execute("SELECT owner FROM bots WHERE token = (?)", (self.token,)).fetchone()[0]
            prefix = cursor.execute("SELECT prefix FROM bots WHERE token = (?)", (self.token,)).fetchone()[0]
            print(f'Login success! ')


    def id(self):
        """This function outputs the bot id"""
        id = cursor.execute("SELECT id FROM bots WHERE token = (?)", (self.token,)).fetchone()[0]
        print(id)


    def name(self):
        """This function outputs the name of the bot"""
        name = cursor.execute("SELECT name FROM bots WHERE token = (?)", (self.token,)).fetchone()[0]
        print(name)


    def owner(self):
        """This function outputs the owner of the bot"""
        owner = cursor.execute("SELECT owner FROM bots WHERE token = (?)", (self.token,)).fetchone()[0]
        print(owner)


    def prefix(self):
        """This function outputs the bot prefix"""
        prefix = cursor.execute("SELECT prefix FROM bots WHERE token = (?)", (self.token,)).fetchone()[0]
        print(prefix)