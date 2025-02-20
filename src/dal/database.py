import psycopg as pg

from src.config import conninfo
db_conn = pg.connect("dbname=postgres user=postgres password=postgres")