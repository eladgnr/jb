# Ensure DB connection is properly imported
from src.dal.db_conn import get_connection
from src.dal.db_conn import get_connection  # Works with direct execution


def create_vacations_table():
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS vacations (
                vacation_id SERIAL PRIMARY KEY,
                country_id INTEGER REFERENCES countries(country_id),
                description VARCHAR(255) NOT NULL,
                start_date DATE NOT NULL,
                end_date DATE NOT NULL,
                price NUMERIC NOT NULL,
                image_name VARCHAR(100) NOT NULL
            )
        """)
        cur.execute("""
            INSERT INTO vacations (country_id, description, start_date, end_date, price, image_name)
            VALUES
            (1, 'Explore the Great Barrier Reef.', '2024-06-01', '2024-06-10', 2500, 'sydney.png'),
            (2, 'Visit the Amazon Rainforest.', '2024-07-05', '2024-07-15', 2000, 'amazon.png'),
            (3, 'Ski trip to Whistler, Canada.', '2024-12-10', '2024-12-20', 3000, 'whistler.png'),
            (4, 'Hike the Great Wall of China.', '2024-09-01', '2024-09-10', 1800, 'greatwall.png'),
            (5, 'Wine tour in France.', '2024-10-01', '2024-10-10', 2200, 'paris.png'),
            (6, 'Oktoberfest in Germany.', '2024-09-15', '2024-09-30', 1500, 'munich.png'),
            (7, 'Taj Mahal sightseeing.', '2024-11-10', '2024-11-20', 1200, 'tajmahal.png'),
            (8, 'Cherry blossom festival.', '2024-03-15', '2024-03-25', 2000, 'tokyo.png'),
            (9, 'Safari in South Africa.', '2024-08-10', '2024-08-20', 3200, 'kruger.png'),
            (10, 'Road trip in the USA.', '2024-06-10', '2024-07-10', 4000, 'route66.png')
            ON CONFLICT DO NOTHING
        """)
        conn.commit()
        cur.close()
        conn.close()


def get_all_vacations():
    """Fetch all vacations from the database."""
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        # Assuming 'vacations' is the table name
        cur.execute("SELECT * FROM vacations")
        vacations = cur.fetchall()
        cur.close()
        conn.close()
        return vacations  # Returns a list of vacation records
    return []


def create_vacation(destination, start_date, end_date, user_id):
    """Insert a new vacation into the database."""
    conn = get_connection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO vacations (destination, start_date, end_date, user_id)
            VALUES (%s, %s, %s, %s)
            RETURNING vacation_id;
        """, (destination, start_date, end_date, user_id))

        vacation_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return vacation_id  # Return the new vacation ID
    return None


if __name__ == "__main__":
    create_vacations_table()
