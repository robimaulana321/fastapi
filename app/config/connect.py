import mysql.connector

# koneksi db lokal
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3307",
    database="user_authentication"
)