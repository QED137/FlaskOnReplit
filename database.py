from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime, text
from sqlalchemy.engine import result

db_coonection_string = "mysql+pymysql://MyFirstDb_rockyareus:9cbe3a9ff75f39a1c3980fffe5147efb5b7f4288@kil.h.filess.io:3307/MyFirstDb_rockyareus?charset=utf8mb4"
engine = create_engine(db_coonection_string)
'''db_connection_string = "mysql+pymysql://<username>:<password>@<host>:<port>/<database_name>?charset=utf8mb4"
engine = create_engine(db_connection_string)
'''
                       
                
  
with engine.connect() as conn:
  result= conn.execute(text("SELECT * FROM posts"))
  print(result.all())
#print(type(engine))