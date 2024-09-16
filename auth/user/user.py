import bcrypt 
import sqlite3

#connecting to db and create a table 
con = sqlite3.connect('auth/dbUser/dbUser.db')
cur = con.cursor()
cur.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
''')

#registering a user
def registerUser(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        cur.execute('''
            INSERT INTO users (username, hashed_password)
            VALUES (?, ?)
        ''', (username, hashed_password,))
        con.commit()
        return True
    except sqlite3.IntegrityError:
        print("\nUsername already exists.Enter a new username\n")
    
    return False

    

#verify user
def verifyUser(username , password):
    
    cur.execute('''
        SELECT hashed_password FROM users WHERE username = ?
''' , (username,))
    response  = cur.fetchone()
    if response is None:
        return False
    hashed_password = response[0]

    if bcrypt.checkpw(password.encode('utf-8') , hashed_password):
        return True
    return False

