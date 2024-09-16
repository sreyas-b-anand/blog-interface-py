import sqlite3

def createTable():
    conn = sqlite3.connect('operations/dbBlog/dbBlog.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS blogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            date TEXT NOT NULL,
            author TEXT NOT NULL
        )
    ''')
    conn.commit()
    