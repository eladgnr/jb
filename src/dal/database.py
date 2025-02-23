import psycopg as pg


# check if connection to db is ok, if so print ok
from src.config import con_info
db_conn = pg.connect("dbname=nw user=admin password=1234")

# create new database name test
db_conn.execute("CREATE DATABASE test")
