import sqlite3 as sq

def create_table():
    with sq.connect('DataBase/feed_back.db') as db:
        db.execute('''CREATE TABLE IF NOT EXISTS feed_back (
                   first_name TEXT NOT NULL,
                   last_name TEXT NOT NULL,
                   user_name TEXT NOT NULL,
                   message_text TEXT NOT NULL
                   )''')
        db.commit()
        