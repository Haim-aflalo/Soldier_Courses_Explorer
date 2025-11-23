import connection
cnx = connection.connect_to_db()
cursor = cnx.cursor()
cursor.execute("""SELECT id, institution, city, course, district, telephone, email
                FROM courses
                LIMIT 1;""")
print(cursor.fetchall())