import db.connection

cnx = db.connection.connect_to_db()
cursor = cnx.cursor()


def search_by_institution():
    target = input("enter the institution")
    cursor.execute("""SELECT id, institution, city, course, district, telephone
                    FROM courses
                    WHERE `institution` LIKE  CONCAT('%',%s,'%')
                    LIMIT 50;""", (target,))

    print(cursor.fetchall())


def search_by_course():
    target = input("enter the course")
    cursor.execute("""SELECT id, institution, city, course, district, telephone
                       FROM courses
                       WHERE `course` LIKE  CONCAT('%',%s,'%')
                       LIMIT 50;""", (target,))

    print(cursor.fetchall())


def search_max_course():
    cursor.execute("""SELECT course, COUNT(*) AS num
                    FROM courses
                    GROUP BY course
                    ORDER BY num DESC
                    LIMIT 1;""")

    print(cursor.fetchall())


def search_min_course():
    cursor.execute("""SELECT course, COUNT(*) AS num
                    FROM courses
                    GROUP BY course
                    ORDER BY num ASC
                    LIMIT 1;""")

    print(cursor.fetchall())


def search_top5_course():
    cursor.execute("""SELECT course, COUNT(*) AS num
                    FROM courses
                    GROUP BY course
                    ORDER BY num DESC
                    LIMIT 5;""")

    print(cursor.fetchall())


def course_count():
    cursor.execute("""SELECT district, COUNT(*) AS num_courses
                        FROM courses
                        GROUP BY district
                        ORDER BY num_courses DESC
                        LIMIT 5;""")

    print(cursor.fetchall())


def queries():
    request = input('enter the request')
    validate = request.startswith("SELECT")
    if validate:
        if  'SELECT * FROM courses WHERE institution LIKE ' in request:
            return search_by_institution()

        if 'SELECT * FROM courses WHERE course LIKE 'in request :
            return search_by_course()

        if request == """SELECT course, COUNT(*) AS num
                    FROM courses
                    GROUP BY course
                    ORDER BY num DESC
                    LIMIT 1;""":
            return search_max_course()

        if request == """SELECT course, COUNT(*) AS num
                    FROM courses
                    GROUP BY course
                    ORDER BY num ASC
                    LIMIT 1;""":
            return search_min_course()

        if request == """SELECT course, COUNT(*) AS num
                    FROM courses
                    GROUP BY course
                    ORDER BY num DESC
                    LIMIT 5;""":
            return search_top5_course()

        if request == """SELECT course, COUNT(*) AS num_courses
                    FROM courses
                    GROUP BY course
                    ORDER BY num_courses DESC
                    LIMIT 5;""":
           return course_count()
        return None

    else:
        return "nothing to do"
