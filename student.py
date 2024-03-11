import mysql.connector

connection_params = {
    "host": "localhost",
    "user": "root",
    "password": "Captain224#",
    "database": "edu_institute",
}

# Establish a connection to the MySQL server
connection = mysql.connector.connect(**connection_params)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Define the SQL query to create the 'students' table
create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    gender CHAR(1),
    enrollment_date DATE,
    program VARCHAR(50)
)
"""

# Execute the SQL query to create the 'students' table
cursor.execute(create_table_query)


# Commit the changes and close the connection

connection.commit()
connection.close()

print("Database 'edu_institute' created successfully.")