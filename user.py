import sqlite3

db = sqlite3.connect('DB/users.sqlite3')
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)""")

class UserAdd():
    """This function creates a new user and adds it to the database"""
    def __init__(self, username, password):
        """Initializing function"""
        self.username = username
        self.password = password
        rows_count = cursor.execute(f"SELECT COUNT() FROM users").fetchone()[0]

        if rows_count == 0:
            last_id = 0
        else:
            last_id = cursor.execute(f"SELECT id FROM users").fetchall()[-1:][0][0]


        cursor.execute("INSERT INTO users VALUES(?, ?, ?)", (last_id+1, self.username, self.password))
        db.commit()

        print(f'Пользователь зарегистрирован\nID: {last_id+1}\nИмя пользователя: {self.username}\nПароль: {self.password}')