import sqlite3

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
