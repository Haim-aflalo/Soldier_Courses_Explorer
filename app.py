import db.connection
import db.queries


def print_menu():
    menu = """Load CSV into DB .1
    Search records by institution name .2
    Search records by course name .3
    Find least common course .4
    Find most common course .5
    Show course count per district .6
    Free SQL query .7
    Exit .8"""
    print(menu)


def play():
    while True:
        print_menu()
        choice = input("Choose option: ")

        if choice == "1":
            print(db.connection.connect_to_db())
            continue

        if choice == "2":
            db.queries.search_by_institution()
            continue

        if choice == "3":
            db.queries.search_by_course()
            continue

        if choice == '4':
            db.queries.search_min_course()
            continue

        if choice == '5':
            db.queries.search_max_course()
            continue

        if choice == '6':
            db.queries.course_count()
            continue
        if choice == '7':
            db.queries.queries()
            continue

        if choice == '8':
            break


play()
