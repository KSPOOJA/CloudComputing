import sqlite3
from sqlalchemy import create_engine, MetaData, Table
import pymysql

# SQLite database file
sqlite_db = 'sqlite:///path_to_your_sqlite_db.db'  # Update this with the actual path to your SQLite database file

# MySQL database configuration
mysql_db = 'mysql+pymysql://admin:CloudComputing2024@mydatabase.cvca4k4ky46o.us-east-1.rds.amazonaws.com/mydatabase'

# Create SQLite engine
sqlite_engine = create_engine(sqlite_db)

# Create MySQL engine
mysql_engine = create_engine(mysql_db)

# Reflect the existing SQLite database
metadata = MetaData()
metadata.reflect(bind=sqlite_engine)

# Create the tables in MySQL
metadata.create_all(mysql_engine)

# Connect to both databases
sqlite_conn = sqlite_engine.connect()
mysql_conn = mysql_engine.connect()

# Transfer data from SQLite to MySQL
for table in metadata.tables.values():
  data = sqlite_conn.execute(table.select()).fetchall()
  if data:
    mysql_conn.execute(table.insert(), data)

# Close connections
sqlite_conn.close()
mysql_conn.close()
