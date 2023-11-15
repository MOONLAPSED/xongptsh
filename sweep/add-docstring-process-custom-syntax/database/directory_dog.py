import sqlite3
import os

def create_engine():
    """
    This function creates and returns a new SQLite3 engine. 
    It takes no parameters and returns an engine object.
    """
    conn = sqlite3.connect('file_info.db')
    return conn

def create_table(conn):
    """
    This function creates a table in the SQLite3 database for storing directory and file information.
    Each row in the table represents a single directory or file.
    """
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS file_info (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        path TEXT NOT NULL,
        size INTEGER NOT NULL
    )
    """)
    conn.commit()

def add_file_info(conn, name, path, size):
    """
    This function adds a row to the file_info table in the SQLite3 database.
    Each row represents a single directory or file.
    """
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO file_info (name, path, size) VALUES (?, ?, ?)
    """, (name, path, size))
    conn.commit()

def iterate_files(conn, directory):
    """
    This function iterates over all files in the given directory and adds their information to the table.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            add_file_info(conn, file, path, size)
