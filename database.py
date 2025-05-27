from functools import partialmethod
import sqlalchemy
from sqlalchemy import create_engine, text
import os


my_secret = os.environ['GOOGLE_MYSQL_DB']


engine = create_engine(my_secret)

# Test the connection by trying to connect
try:
    with engine.connect() as connection:
        print("Connection successful!")
        # You can also execute a test query
        result = connection.execute(text("SELECT * from jobs"))
        #print(result.all()[0])
        result_dicts = []
        for row in result.all():
            result_dicts.append(dict(zip(result.keys(), row)))
        print(result_dicts)    
        #print(result.all())  # Should print (1,)
        #print(type(result))
        #print(type(result.all()))
        #print(result.all())
except Exception as e:
    print(f"Connection failed: {e}")

def load_data_from_db():
  with engine.connect() as conn:
    # Execute a SQL query to select all rows from the 'posts' table
    result = conn.execute(text("SELECT * FROM jobs"))

    # Fetch column names from the query result
    columns = result.keys()  

    # Convert the query result into a list of dictionaries, with column names as keys
    result_dicts = [dict(zip(columns, row)) for row in result.fetchall()]

    # Print the list of dictionaries representing the query result
    return result_dicts

def load_job_fromDB(id):
    # Connecting to the database and executing the query
    with engine.connect() as conn:
        # Executing SQL query with a placeholder for the job ID
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id})

        # Fetching the first row
        row = result.fetchone()

        # Check if row is found
        if row is None:
            return None
        else:
            # Convert row into a dictionary using column names as keys
            return dict(zip(result.keys(), row))
        
        
result1 = load_data_from_db()
print(result1[1])