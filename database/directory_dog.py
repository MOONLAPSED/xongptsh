import sqlite3


def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn, cursor


def create_tables(cursor):
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

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS permissions (
            id INTEGER PRIMARY KEY,
            file_id INTEGER,
            user_id INTEGER,
            permission TEXT,
            FOREIGN KEY (file_id) REFERENCES files (id),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    """
    )


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

    cursor.execute(
        """
        INSERT INTO directories (name, path, created_at, modified_at)
        VALUES ('dir1', '/path/to/dir1', '2021-01-01', '2021-01-02')
    """
    )

    cursor.execute(
        """
        INSERT INTO directories (name, path, created_at, modified_at)
        VALUES ('dir2', '/path/to/dir2', '2021-01-03', '2021-01-04')
    """
    )

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

    cursor.execute(
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
