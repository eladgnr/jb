from src.dal.database import db_conn

import psycopg.sql
import psycopg.rows as pgrows

class UserDAO:
    def get_all_users(self):
        with db_conn.cursor() as cur:
            cur.execute(psycopg.sql.SQL"SELECT * FROM {} ;")
                        .format(psycopg.sql.Identifier(self.table_name))
            
