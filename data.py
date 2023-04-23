#To check if Connected to the database or not
import psycopg2

try:
    conn = psycopg2.connect(
        dbname="mad",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    print("Connected to database successfully!")
    conn.close()
except psycopg2.Error as e:
    print("Unable to connect to database")
    print(e)
