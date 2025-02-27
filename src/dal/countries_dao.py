from db_conn import get_connection


def create_countries_table():
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE countries (
                country_id SERIAL PRIMARY KEY,
                country_name VARCHAR(50) NOT NULL,
                description VARCHAR(255)
            )
        """)
        cur.execute("""
            INSERT INTO countries (country_name, description) 
            VALUES 
            ('Australia', 'A land of kangaroos and vast deserts.'),
            ('Brazil', 'Famous for its carnival and vibrant culture.'),
            ('Canada', 'Known for its natural beauty and maple syrup.'),
            ('China', 'Home to the Great Wall and rich history.'),
            ('France', 'Land of wine, cheese, and the Eiffel Tower.'),
            ('Germany', 'Renowned for its engineering and Oktoberfest.'),
            ('India', 'Diverse culture and the Taj Mahal.'),
            ('Japan', 'Known for technology and cherry blossoms.'),
            ('South Africa', 'Famous for its wildlife and Nelson Mandela.'),
            ('United States', 'Land of opportunities and diverse culture.')
        """)
        conn.commit()
        cur.close()
        conn.close()


if __name__ == "__main__":
    create_countries_table()
