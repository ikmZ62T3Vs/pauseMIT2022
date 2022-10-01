import sqlite3

connection = sqlite3.connect('database.db')


with open('time_stamps.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO video_watch time VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )


connection.commit()
connection.close()