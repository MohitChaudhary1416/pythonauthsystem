import sqlite3

class DBHelper:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        query = '''
                    CREATE TABLE IF NOT EXISTS USER (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                    )
                '''    
        self.cursor.execute(query)
        self.connection.commit()

    def get_user(self, username):
        query = f'''
                    SELECT username,password FROM USER where username = '{username}'
                '''
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user
    
    def add_user(self, username, password):
        query = f'''
                    INSERT INTO USER (username, password) VALUES ('{username}', '{password}')
                '''
        self.cursor.execute(query)
        self.connection.commit()