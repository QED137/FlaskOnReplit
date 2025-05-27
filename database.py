from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime, text
from sqlalchemy.engine import result
import os
import logging
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql+pymysql://myfirstDB_goprettywe:b5f69eae773cb5af8088dcefc48e1e17ce71e8f0@8zg.h.filess.io/myfirstDB_goprettywe?charset=utf8mb4")
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
def load_job_fromDB(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM posts WHERE id = :val"), {"val": id})
        rows = result.fetchall()
        if len(rows) == 0:
            return None
        else:
            return rows[0]

print(load_job_fromDB(1))
#the following code is for retriveing data from the webpage and psuhing it into the database

