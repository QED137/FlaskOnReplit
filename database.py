from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime, text
from sqlalchemy.engine import result
import os

db_coonection_string = os.environ["DATABASE_CONNECT_STRING"] #keeping safe
engine = create_engine(db_coonection_string)

'''with engine.connect() as conn:
  result= conn.execute(text("SELECT * FROM posts"))
  print("type(result)",type(result))
  print(result.all())
  print("print(type(result.all()))",type(result.all()))'''
#print(type(engine))
#how to get data back from mysql
# Establish a connection to the database and execute a query
def load_data_from_db():
  with engine.connect() as conn:
    # Execute a SQL query to select all rows from the 'posts' table
    result = conn.execute(text("SELECT * FROM posts"))

    # Fetch column names from the query result
    columns = result.keys()  

    # Convert the query result into a list of dictionaries, with column names as keys
    result_dicts = [dict(zip(columns, row)) for row in result.fetchall()]

    # Print the list of dictionaries representing the query result
    return result_dicts