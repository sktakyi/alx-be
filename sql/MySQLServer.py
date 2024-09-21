import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS alx_book_store DEFAULT CHARACTER SET 'utf8'"
        )
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

def main():
    try:
        # Connect to MySQL server
        db = mysql.connector.connect(
            user='your_username',       
            password='your_password',   
            host='localhost'            
        )
        cursor = db.cursor()

        # Create database
        create_database(cursor)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        # Close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()

if __name__ == "__main__":
    main()