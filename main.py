
from database_operations import connect_to_database, create_table, insert_data, modify_data, delete_data, view_data, close_connection

def main():

    connection = connect_to_database()

    cursor = connection.cursor()

    create_table(cursor)

    while True:
        print("\nTabs:")
        print("1. Insert Data")
        print("2. Modify Data")
        print("3. Delete Data")
        print("4. View Data")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            insert_data(connection, cursor)
        elif choice == "2":
            modify_data(connection, cursor)
        elif choice == "3":
            delete_data(connection, cursor)
        elif choice == "4":
            view_data(cursor)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


    close_connection(connection, cursor)

if __name__ == "__main__":
    main()
