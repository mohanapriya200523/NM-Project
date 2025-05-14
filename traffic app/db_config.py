import mysql.connector # type: ignore

def get_connection():
    return mysql.connector.connect(
        host="localhost",          # or your MySQL server
        user="root",
        password="mohanapriya@23",
        database="traffic_db"
    )
