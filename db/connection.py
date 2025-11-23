import mysql.connector


def connect_to_db():
    cnx = mysql.connector.connect(
    user = "root" , password = "" , host = "127.0.0.1" , database = "project_db" 
    )

    print("connected, server version:", cnx.get_server_info())
    return cnx
