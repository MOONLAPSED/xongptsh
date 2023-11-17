import unittest
from unittest.mock import MagicMock
from database.pyschema import insert_data


import unittest
from unittest.mock import MagicMock
from database import pyschema


class TestInsertData(unittest.TestCase):
    def setUp(self):
        self.cursor = MagicMock()

    def test_insert_data(self):
        insert_data(self.cursor)
        self.assertEqual(self.cursor.execute.call_count, 8)

    def test_insert_data(self):
        insert_data(self.cursor)
        self.assertEqual(self.cursor.execute.call_count, 8)

        # Check the arguments of the execute method calls
        calls = self.cursor.execute.call_args_list

        # Check the SQL commands for inserting into the files table
        self.assertIn("INSERT INTO files", calls[0][0][0])
        self.assertIn("INSERT INTO files", calls[1][0][0])

        # Check the SQL commands for inserting into the directories table
        self.assertIn("INSERT INTO directories", calls[2][0][0])
        self.assertIn("INSERT INTO directories", calls[3][0][0])

        # Check the SQL commands for inserting into the permissions table
        self.assertIn("INSERT INTO permissions", calls[4][0][0])
        self.assertIn("INSERT INTO permissions", calls[5][0][0])

        # Check the SQL commands for inserting into the users table
        self.assertIn("INSERT INTO users", calls[6][0][0])
        self.assertIn("INSERT INTO users", calls[7][0][0])

    def test_insert_data(self):
        insert_data(self.cursor)
        self.assertEqual(self.cursor.execute.call_count, 8)

        # Check the arguments of the execute method calls
        calls = self.cursor.execute.call_args_list

        # Check the SQL commands for inserting into the files table
        self.assertIn("INSERT INTO files", calls[0][0][0])
        self.assertIn("INSERT INTO files", calls[1][0][0])

        # Check the SQL commands for inserting into the directories table
        self.assertIn("INSERT INTO directories", calls[2][0][0])
        self.assertIn("INSERT INTO directories", calls[3][0][0])

        # Check the SQL commands for inserting into the permissions table
        self.assertIn("INSERT INTO permissions", calls[4][0][0])
        self.assertIn("INSERT INTO permissions", calls[5][0][0])

        # Check the SQL commands for inserting into the users table
        self.assertIn("INSERT INTO users", calls[6][0][0])
        self.assertIn("INSERT INTO users", calls[7][0][0])

    def test_insert_data_exception(self):
        self.cursor.execute.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            insert_data(self.cursor)
        self.assertTrue("Database error" in str(context.exception))

    def test_insert_data(self):
        insert_data(self.cursor)
        self.assertEqual(self.cursor.execute.call_count, 8)

        # Check the arguments of the execute method calls
        calls = self.cursor.execute.call_args_list

        # Check the SQL commands for inserting into the files table
        self.assertIn("INSERT INTO files", calls[0][0][0])
        self.assertIn("INSERT INTO files", calls[1][0][0])

        # Check the SQL commands for inserting into the directories table
        self.assertIn("INSERT INTO directories", calls[2][0][0])
        self.assertIn("INSERT INTO directories", calls[3][0][0])

        # Check the SQL commands for inserting into the permissions table
        self.assertIn("INSERT INTO permissions", calls[4][0][0])
        self.assertIn("INSERT INTO permissions", calls[5][0][0])

        # Check the SQL commands for inserting into the users table
        self.assertIn("INSERT INTO users", calls[6][0][0])
        self.assertIn("INSERT INTO users", calls[7][0][0])

    def test_insert_data_exception(self):
        self.cursor.execute.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            insert_data(self.cursor)
        self.assertTrue("Database error" in str(context.exception))

    def test_insert_data_no_cursor(self):
        with self.assertRaises(TypeError) as context:
            insert_data(None)
        self.assertTrue("cursor object is None" in str(context.exception))

    def test_insert_data(self):
        insert_data(self.cursor)
        self.assertEqual(self.cursor.execute.call_count, 8)

        # Check the arguments of the execute method calls
        calls = self.cursor.execute.call_args_list

        # Check the SQL commands for inserting into the files table
        self.assertIn("INSERT INTO files", calls[0][0][0])
        self.assertIn("INSERT INTO files", calls[1][0][0])

        # Check the SQL commands for inserting into the directories table
        self.assertIn("INSERT INTO directories", calls[2][0][0])
        self.assertIn("INSERT INTO directories", calls[3][0][0])

        # Check the SQL commands for inserting into the permissions table
        self.assertIn("INSERT INTO permissions", calls[4][0][0])
        self.assertIn("INSERT INTO permissions", calls[5][0][0])

        # Check the SQL commands for inserting into the users table
        self.assertIn("INSERT INTO users", calls[6][0][0])
        self.assertIn("INSERT INTO users", calls[7][0][0])

    def test_insert_data_exception(self):
        self.cursor.execute.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            insert_data(self.cursor)
        self.assertTrue("Database error" in str(context.exception))

    def test_insert_data_no_cursor(self):
        with self.assertRaises(TypeError) as context:
            insert_data(None)
        self.assertTrue("cursor object is None" in str(context.exception))

    def test_insert_data_no_execute_method(self):
        del self.cursor.execute
        with self.assertRaises(AttributeError) as context:
            insert_data(self.cursor)
        self.assertTrue(
            "'MagicMock' object has no attribute 'execute'" in str(context.exception)
        )


class TestCreateTables(unittest.TestCase):
    def setUp(self):
        self.cursor = MagicMock()

    def test_create_tables(self):
        pyschema.create_tables(self.cursor)
        self.cursor.execute.assert_any_call(
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
        self.cursor.execute.assert_any_call(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        """
        )

    def test_create_tables(self):
        pyschema.create_tables(self.cursor)
        self.cursor.execute.assert_any_call(
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
        self.cursor.execute.assert_any_call(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        """
        )

    def test_create_tables_exception(self):
        self.cursor.execute.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            pyschema.create_tables(self.cursor)
        self.assertTrue("Database error" in str(context.exception))

    def test_create_tables(self):
        pyschema.create_tables(self.cursor)
        self.cursor.execute.assert_any_call(
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
        self.cursor.execute.assert_any_call(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        """
        )

    def test_create_tables_exception(self):
        self.cursor.execute.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            pyschema.create_tables(self.cursor)
        self.assertTrue("Database error" in str(context.exception))

    def test_create_tables_no_cursor(self):
        with self.assertRaises(TypeError) as context:
            pyschema.create_tables(None)
        self.assertTrue("cursor object is None" in str(context.exception))

    def test_create_tables(self):
        pyschema.create_tables(self.cursor)
        self.cursor.execute.assert_any_call(
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
        self.cursor.execute.assert_any_call(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        """
        )

    def test_create_tables_exception(self):
        self.cursor.execute.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            pyschema.create_tables(self.cursor)
        self.assertTrue("Database error" in str(context.exception))

    def test_create_tables_no_cursor(self):
        with self.assertRaises(TypeError) as context:
            pyschema.create_tables(None)
        self.assertTrue("cursor object is None" in str(context.exception))

    def test_create_tables_no_execute_method(self):
        del self.cursor.execute
        with self.assertRaises(AttributeError) as context:
            pyschema.create_tables(self.cursor)
        self.assertTrue(
            "'MagicMock' object has no attribute 'execute'" in str(context.exception)
        )

    def test_create_tables(self):
        pyschema.create_tables(self.cursor)
        self.cursor.execute.assert_any_call(
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
        self.cursor.execute.assert_any_call(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        """
        )
        self.assertEqual(self.cursor.execute.call_count, 2)

    def test_create_tables_exception(self):
        self.cursor.execute.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            pyschema.create_tables(self.cursor)
        self.assertTrue("Database error" in str(context.exception))

    def test_create_tables_no_cursor(self):
        with self.assertRaises(TypeError) as context:
            pyschema.create_tables(None)
        self.assertTrue("cursor object is None" in str(context.exception))

    def test_create_tables_no_execute_method(self):
        del self.cursor.execute
        with self.assertRaises(AttributeError) as context:
            pyschema.create_tables(self.cursor)
        self.assertTrue(
            "'MagicMock' object has no attribute 'execute'" in str(context.exception)
        )


if __name__ == "__main__":
    unittest.main()
