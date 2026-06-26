import sqlite3

DB_NAME = "movies.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_id TEXT NOT NULL,
            file_type TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_movie(file_id, file_type):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movies (file_id, file>
    movie_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return movie_id

def get_movie(movie_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT file_id, file_type FROM mo>
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"file_id": row[0], "file_type": row[1>
    return None
  
