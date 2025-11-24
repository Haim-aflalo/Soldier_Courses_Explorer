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
        match choice:
            case "1":
                print(db.connection.connect_to_db())
                continue

            case "2":
                db.queries.search_by_institution()
                continue

            case "3":
                db.queries.search_by_course()
                continue

            case '4':
                db.queries.search_min_course()
                continue

            case '5':
                db.queries.search_max_course()
                continue

            case '6':
                db.queries.course_count()
                continue
            case '7':
                db.queries.queries()
                continue

            case '8':
                break


if __name__ == "__main__":
    play()
