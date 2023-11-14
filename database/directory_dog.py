# Define database connection parameters
db_type = "database_type"
host = "host"
port = "port"
username = "username"
password = "password"
database_name = "database_name"

"""
Create a database connection using the defined parameters.

Parameters:
db_type (str): The type of the database.
username (str): The username for the database.
password (str): The password for the database.
host (str): The host of the database.
port (str): The port of the database.
database_name (str): The name of the database.

Returns:
engine: The created database connection.
"""
engine = create_engine(f"{db_type}://{username}:{password}@{host}:{port}/{database_name}")

# Define table schema
table_schema = """
CREATE TABLE IF NOT EXISTS file_data (
    filename VARCHAR(255),
    file_type VARCHAR(10),
    content TEXT,
    other_info VARCHAR(255)
);
"""

"""
Execute the table creation query using the created database connection.

Parameters:
engine: The created database connection.
table_schema (str): The table schema to be created.

Returns:
None
"""
with engine.connect() as conn:
    conn.execute(table_schema)

# Define directory path
directory_path = "path/to/linux/files"

"""
Iterate over files in the directory, check if the file is .md or .txt, read file contents into a DataFrame, and insert data into the database table.

Parameters:
directory_path (str): The path to the directory.
engine: The created database connection.

Returns:
None
"""
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    
    if filename.endswith(".md") or filename.endswith(".txt"):
        
        df = pd.DataFrame()
        with open(file_path, "r") as file:
            content = file.read()
            df = df.append({"filename": filename, "file_type": os.path.splitext(filename)[1], "content": content}, ignore_index=True)
        
        df.to_sql("file_data", engine, if_exists="append", index=False)
"""
This module defines the database connection parameters, creates a database connection, defines a table schema, executes the table creation query, defines a directory path, iterates over files in the directory, checks if the file is .md or .txt, reads file contents into a DataFrame, and inserts data into the database table.
"""
=======