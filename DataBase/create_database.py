import sqlite3 as sq

def create_table():
    with sq.connect('DataBase/feed_back.db') as db:
        db.execute('''CREATE TABLE IF NOT EXISTS feed_back (
                   first_name TEXT,
                   last_name TEXT,
                   user_name TEXT,
                   message_text TEXT 
                   )''')
        db.commit()
        