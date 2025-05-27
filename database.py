# '''from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime, text
# from sqlalchemy.engine import result
# import os
# import logging
# from sqlalchemy.exc import SQLAlchemyError

# engine = create_engine("mysql+pymysql://myfirstDB_goprettywe:b5f69eae773cb5af8088dcefc48e1e17ce71e8f0@8zg.h.filess.io/myfirstDB_goprettywe?charset=utf8mb4")
# #print(type(engine))
# #how to get data back from mysql
# # Establish a connection to the database and execute a query
# def load_data_from_db():
#   with engine.connect() as conn:
#     # Execute a SQL query to select all rows from the 'posts' table
#     result = conn.execute(text("SELECT * FROM posts"))

#     # Fetch column names from the query result
#     columns = result.keys()  

#     # Convert the query result into a list of dictionaries, with column names as keys
#     result_dicts = [dict(zip(columns, row)) for row in result.fetchall()]

#     # Print the list of dictionaries representing the query result
#     return result_dicts
# def load_job_fromDB(id):
#     with engine.connect() as conn:
#         result = conn.execute(text("SELECT * FROM posts WHERE id = :val"), {"val": id})
#         rows = result.fetchall()
#         if len(rows) == 0:
#             return None
#         else:
#             return rows[0]

# print(load_job_fromDB(1))
# #the following code is for retriveing data from the webpage and psuhing it into the database

# '''
# import os
# import psycopg2
# from flask import Flask, render_template
# def get_db_connection():
#     return psycopg2.connect(
#         host='dpg-cq95unrv2p9s73cdvrv0-a',
#         database='myfirstdb_gaoa',
#         user=os.getenv('DATABASE_USER', 'jay'),
#         password=os.getenv('DATABASE_PASSWORD', 'oDv9xYgw1cywbb6WASW9wM9BHiUoeILs')
#     )

# try:
#     conn = get_db_connection()
#     print("Connection successful")
#     conn.close()
# except Exception as e:
#     print(f"Error connecting to the database: {e}")

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
result1 = load_data_from_db()
print(result1[1])