import sqlite3

connection = sqlite3.connect('blog.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Erster Post', 'Das hier ist der allererste Post in unserem Blog.')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Zweiter Post', 'Und das ist auch schon der nächste Beitrag.')
            )

connection.commit()
connection.close()