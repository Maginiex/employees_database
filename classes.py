import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()

connect.commit()


class Create_database:
    def create(self):
        cursor.execute("CREATE TABLE IF NOT EXISTS users(number INTEGER)")
        all_results = cursor.fetchall()


class Add_database:
    def add(self):
        cursor.execute("INSERT INTO users(number) VALUES (120)")
        connect.commit()


class Delete_database:
    def delete(self):
        cursor.execute("DROP TABLE users")
        connect.commit()

table = Create_database()
table.create()