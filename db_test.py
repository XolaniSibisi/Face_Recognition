import mysql.connector

try:
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="face_recognizer")
    print("Connected to the database!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Database connection closed.")
