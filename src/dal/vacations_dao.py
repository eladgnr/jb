from db_conn import get_connection


def create_vacations_table():
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE vacations (
                vacation_id SERIAL PRIMARY KEY,
                country_id INTEGER REFERENCES countries(country_id),
                description VARCHAR(255),
                start_date DATE,
                end_date DATE,
                price NUMERIC,
                image_name VARCHAR(100)
            )
        """)
        cur.execute("""
            INSERT INTO vacations (country_id, description, start_date, end_date, price, image_name) 
            VALUES 
            (1, 'Relaxing beaches and vibrant city life', '2023-06-01', '2023-06-10', 1500, 'sydney.png'),
            (2, 'Exploring the Amazon rainforest', '2023-07-01', '2023-07-15', 2000, 'amazon.png')
        """)
        conn.commit()
        cur.close()
        conn.close()


if __name__ == "__main__":
    create_vacations_table()
