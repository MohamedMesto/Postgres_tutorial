 
import psycopg2

try:
    # Replace these parameters with your own database credentials
    connection = psycopg2.connect(
        dbname="chinook",
        user="rot_eu_2050",
        password="Fullstack#$2050",
        host="localhost",
        port="5432"
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    
    print(f"Connected to PostgreSQL database, version: {db_version}")
    
    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error connecting to PostgreSQL database: {error}")
