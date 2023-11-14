# Define database connection parameters
db_type = "database_type"
host = "host"
port = "port"
username = "username"
password = "password"
database_name = "database_name"

# Create database connection
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

# Execute table creation query
with engine.connect() as conn:
    conn.execute(table_schema)

# Define directory path
directory_path = "path/to/linux/files"

# Iterate over files in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    
    # Check if file is .md or .txt
    if filename.endswith(".md") or filename.endswith(".txt"):
        
        # Read file contents into DataFrame
        df = pd.DataFrame()
        with open(file_path, "r") as file:
            content = file.read()
            df = df.append({"filename": filename, "file_type": os.path.splitext(filename)[1], "content": content}, ignore_index=True)
        
        # Insert data into database table
        df.to_sql("file_data", engine, if_exists="append", index=False)