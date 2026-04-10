import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        port=int(os.getenv("MYSQLPORT"))
    )

def insert_data(customerID, prediction):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO churn_prediction (customerID, prediction) VALUES (%s, %s)"
    cursor.execute(query, (customerID, prediction))

    conn.commit()
    conn.close()

def fetch_data():
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM churn_prediction"
    cursor.execute(query)

    data = cursor.fetchall()

    conn.close()
    return data