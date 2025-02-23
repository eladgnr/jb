import psycopg2

# Define the connection string
con_info = "postgresql://postgres:1234@localhost:5432/postgres"

try:
    # Connect to the database using the connection string
    db_connection = psycopg2.connect(con_info)
    print("Connection successful!")
except Exception as e:
    print(f"An error occurred: {e}")
