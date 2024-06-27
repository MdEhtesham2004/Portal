# Replace these values with your PostgreSQL connection details
import psycopg2 as pg

db_params = {
    'host': 'localhost',
    'database': 'first_project',
    'user': 'postgres',
    'password': 'ehtesham3007',
    'port': 5433
}

connection = None
cursor = None

try:
    # Connect to the PostgreSQL database
    connection = pg.connect(
        host=db_params['host'],
        database=db_params['database'],
        user=db_params['user'],
        password=db_params['password'],
        port=db_params['port']
    )
    cursor = connection.cursor()
    print("Connected Successfully!")

except Exception as error:
    print("Exception in connection:", error)


def insert_entry(name, email, password):
    try:
        cursor.execute("INSERT INTO RECORDS (NAME, EMAIL, PASSWORD) VALUES (%s, %s, %s)", (name, email, password))
        print("Inserted values successfully!")
        connection.commit()

    except Exception as error:
        print("Exception during insertion:", error)


def check_credentials(email, password):
    try:
        cursor.execute("SELECT * FROM RECORDS WHERE EMAIL = %s AND PASSWORD = %s", (email, password))
        record = cursor.fetchone()
        if record:
            print("Credentials match existing records.")
            return True
        else:
            print("Credentials do not match existing records.")
            return False
    except Exception as error:
        print("Exception during credential check:", error)


# Close connection and cursor
def close_connection():
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
