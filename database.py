import sqlite3

conn = sqlite3.connect("guitar_mania.db")
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        age INTEGER
    );
''')
conn.commit()
conn.close()
