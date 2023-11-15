import sqlite3


def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn, cursor


def create_tables(cursor):
    max_retries = 5
    base_delay = 1
    for retry_count in range(max_retries):
        try:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS files (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    path TEXT,
                    size INTEGER,
                    created_at TEXT,
                    modified_at TEXT
                )
            """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS directories (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    path TEXT,
                    created_at TEXT,
                    modified_at TEXT
                )
            """
            )
        except sqlite3.OperationalError:
            if retry_count >= max_retries - 1:
                raise
            else:
                delay = base_delay * (2 ** retry_count)
                time.sleep(delay)


def insert_data(cursor):
    cursor.execute(
        """
        INSERT INTO files (name, path, size, created_at, modified_at)
        VALUES ('file1.txt', '/path/to/file1.txt', 100, '2021-01-01', '2021-01-02')
    """
    )

    cursor.execute(
        """
        INSERT INTO files (name, path, size, created_at, modified_at)
        VALUES ('file2.txt', '/path/to/file2.txt', 200, '2021-01-03', '2021-01-04')
    """
    )


        """
        INSERT INTO users (name, email)
        VALUES ('user2', 'user2@example.com')
    """
    )


def close_connection(conn):
    conn.commit()
    conn.close()


def main():
    conn, cursor = create_database("unix_file_system.db")
    create_tables(cursor)
    insert_data(cursor)
    close_connection(conn)


if __name__ == "__main__":
    main()
            break
        except sqlite3.OperationalError:
            if retry_count >= max_retries - 1:
                raise
            else:
                delay = base_delay * (2 ** retry_count)
                time.sleep(delay)


def insert_data(cursor):
    max_retries = 5
    base_delay = 1
    for retry_count in range(max_retries):
        try:
                """
                INSERT INTO directories (name, path, created_at, modified_at)
                VALUES ('dir1', '/path/to/dir1', '2021-01-01', '2021-01-02')
            """
            )

            cursor.execute(
    cursor.execute(
        """
        INSERT INTO permissions (file_id, user_id, permission)
        VALUES (1, 1, 'read')
    """
    )

    cursor.execute(
        """
        INSERT INTO permissions (file_id, user_id, permission)
        VALUES (2, 2, 'write')
    """
    )

    cursor.execute(
        """
        INSERT INTO users (name, email)
        VALUES ('user1', 'user1@example.com')
    """
    )



if __name__ == "__main__":
    main()
