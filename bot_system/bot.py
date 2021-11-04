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

class Create():
    """This class creates a new bot and adds it to the database"""
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


class Delete():
    """This class removes the bot"""
    def __init__(self, id, token):
        """Initializing function"""
        self.id = id
        self.token = token

        if cursor.execute("SELECT id FROM bots WHERE id = (?)", (self.id,)).fetchone() is None:
            print('Error! ID is invalid')
        else:
            if cursor.execute("SELECT token FROM bots WHERE id = (?)", (self.id,)).fetchone()[0] == self.token:
                cursor.execute("DELETE FROM bots WHERE id = (?)", (self.id,))
                db.commit()
            else:
                print('Error! Token is invalid')


class Run():
    """This class launches the bot"""
    def __init__(self, token):
        """Initializing function"""

        self.token = token


        if cursor.execute("SELECT token FROM bots WHERE token = (?)", (self.token,)).fetchone() is None:
            print('Error! Token is invalid')
        else:
            pass


    def id(self):
        """This function outputs the bot id"""
        if cursor.execute("SELECT token FROM bots WHERE token = (?)", (self.token,)).fetchone() is None:
            pass
        else:
            id = cursor.execute("SELECT id FROM bots WHERE token = (?)", (self.token,)).fetchone()[0]
            return id


    def name(self):
        """This function outputs the name of the bot"""
        if cursor.execute("SELECT token FROM bots WHERE token = (?)", (self.token,)).fetchone() is None:
            pass
        else:
            name = cursor.execute("SELECT name FROM bots WHERE token = (?)", (self.token,)).fetchone()[0]
            return name


    def owner(self):
        """This function outputs the owner of the bot"""
        if cursor.execute("SELECT token FROM bots WHERE token = (?)", (self.token,)).fetchone() is None:
            pass
        else:
            owner = cursor.execute("SELECT owner FROM bots WHERE token = (?)", (self.token,)).fetchone()[0]
            return owner


    def prefix(self):
        """This function outputs the bot prefix"""
        if cursor.execute("SELECT token FROM bots WHERE token = (?)", (self.token,)).fetchone() is None:
            pass
        else:
            prefix = cursor.execute("SELECT prefix FROM bots WHERE token = (?)", (self.token,)).fetchone()[0]
            return prefix
