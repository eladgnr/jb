import unittest
from src.dal.db_conn import get_connection


class TestDatabaseConnection(unittest.TestCase):

    def setUp(self):
        """Set up a test database connection."""
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def test_connection(self):
        """Test if the database connection is established."""
        self.assertIsNotNone(self.conn, "Database connection failed.")

    def test_tables_exist(self):
        """Check if essential tables exist in the database."""
        tables = ["users", "vacations", "likes", "countries", "roles"]
        for table in tables:
            self.cursor.execute(f"""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables
                    WHERE table_name = '{table}'
                );
            """)
            exists = self.cursor.fetchone()[0]
            self.assertTrue(exists, f"Table {table} does not exist.")

    def test_insert_and_retrieve_user(self):
        """Test inserting a user and retrieving it."""
        self.cursor.execute("""
            INSERT INTO users (first_name, last_name, email, password, job_id)
            VALUES ('Test', 'User', 'test@example.com', 'securepass', 1)
            RETURNING user_id;
        """)
        user_id = self.cursor.fetchone()[0]
        self.conn.commit()

        self.cursor.execute(
            "SELECT * FROM users WHERE user_id = %s;", (user_id,))
        user = self.cursor.fetchone()
        self.assertIsNotNone(user, "User insertion failed.")

    def test_unique_email_constraint(self):
        """Ensure that duplicate emails cannot be inserted."""
        self.cursor.execute("""
            INSERT INTO users (first_name, last_name, email, password, job_id)
            VALUES ('Test', 'User', 'unique@example.com', 'securepass', 1)
            RETURNING user_id;
        """)
        self.conn.commit()

        try:
            self.cursor.execute("""
                INSERT INTO users (first_name, last_name, email, password, job_id)
                VALUES ('Duplicate', 'User', 'unique@example.com', 'securepass', 1);
            """)
            self.conn.commit()
            self.fail("Duplicate email was inserted despite unique constraint.")
        except Exception:
            self.conn.rollback()  # Rollback transaction on failure

    def tearDown(self):
        """Clean up test data and close the database connection."""
        self.cursor.execute(
            "DELETE FROM users WHERE email IN ('test@example.com', 'unique@example.com');")
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    unittest.main()
