import os
import sqlite3
import time


def retry_with_backoff(func, *args, max_retries=5, base_delay=0.1, max_delay=5.0):
    """
    This function implements a retry loop with exponential backoff.
    It takes a function and its arguments as parameters, and calls the function with the given arguments.
    If the function raises an exception, it waits for a delay time before retrying.
    The delay time starts at a base delay time and increases exponentially on each retry, up to a maximum delay time.
    The function retries the operation until it succeeds or the maximum number of retries is reached.
    """
    # Removed unnecessary code block
    """
    This function creates a table in the SQLite3 database for storing directory and file information.
    Each row in the table represents a single directory or file.
    """
    cursor = conn.cursor()
    retry_with_backoff(cursor.execute,
            """
        CREATE TABLE IF NOT EXISTS file_info (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            path TEXT NOT NULL,
            size INTEGER NOT NULL
        )
        """
    )
    conn.commit()


        # Removed unnecessary code block
    """
    cursor = conn.cursor()
    retry_with_backoff(cursor.execute,
            """
        INSERT INTO file_info (name, path, size) VALUES (?, ?, ?)
        """,
            (name, path, size),
    )
    conn.commit()


def iterate_files(conn, directory):
    """
    This function iterates over all files in the given directory and adds their information to the table.
    """
    for root, _dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            add_file_info(conn, file, path, size)
    return conn
    # Removed unnecessary code block
