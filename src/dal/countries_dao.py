from src.dal.db_conn import get_connection  # Works with direct execution


def get_all_countries():
    """Fetch all countries from the database."""
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM countries")
        countries = cur.fetchall()
        cur.close()
        conn.close()
        return countries
    return []


def create_countries_table():
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS countries (
                country_id SERIAL PRIMARY KEY,
                country_name VARCHAR(50) UNIQUE NOT NULL,
                description VARCHAR(255) NOT NULL
            )
        """)
        cur.execute("""
            INSERT INTO countries (country_name, description)
            VALUES 
            ('Australia', 'Sunny beaches and kangaroos.'),
            ('Brazil', 'Home of the Amazon rainforest.'),
            ('Canada', 'Maple syrup and vast wilderness.'),
            ('China', 'Great Wall and rich history.'),
            ('France', 'Eiffel Tower and fine wine.'),
            ('Germany', 'Engineering and Oktoberfest.'),
            ('India', 'Diverse culture and Taj Mahal.'),
            ('Japan', 'Technology and cherry blossoms.'),
            ('South Africa', 'Wildlife and beautiful landscapes.'),
            ('United States', 'Big cities and national parks.')
            ON CONFLICT (country_name) DO NOTHING
        """)
        conn.commit()
        cur.close()
        conn.close()


if __name__ == "__main__":
    create_countries_table()
