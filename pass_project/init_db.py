import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (id, email, passcode, passCost,joined_on) VALUES (?,?,?,?,?)",
            ('First user', 'Details for the first user')
            )

cur.execute("INSERT INTO users (id, email, passcode, passCost,joined_on) VALUES (?,?,?,?,?)",
            ('Second user', 'Details for the Second user')
            )

connection.commit()
connection.close()