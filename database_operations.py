
import mysql.connector

def connect_to_database():

    host = "localhost"
    user = "root"
    password = "root"
    database = "python_sql"

    # Connect to the database
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

def create_table(cursor):

    table_creation_query = """
    CREATE TABLE IF NOT EXISTS students (
        student_id INT PRIMARY KEY,
        student_name VARCHAR(100),
        student_address VARCHAR(255),
        student_phone VARCHAR(15)
    )
    """

    cursor.execute(table_creation_query)

def insert_data(connection, cursor):

    student_id = int(input("Enter Student ID: "))
    student_name = input("Enter Student Name: ")
    student_address = input("Enter Student Address: ")
    student_phone = input("Enter Student Phone: ")


    insert_query = """
    INSERT INTO students (student_id, student_name, student_address, student_phone)
    VALUES (%s, %s, %s, %s)
    """

    data = (student_id, student_name, student_address, student_phone)

    cursor.execute(insert_query, data)

    connection.commit()

    print("Data inserted successfully!")

def modify_data(connection, cursor):

    student_id = int(input("Enter Student ID to modify: "))
    new_student_name = input("Enter the new Student Name: ")


    modify_query = """
    UPDATE students
    SET student_name = %s
    WHERE student_id = %s
    """


    data = (new_student_name, student_id)


    cursor.execute(modify_query, data)


    connection.commit()

    print("Data modified successfully!")

def delete_data(connection, cursor):

    student_id = int(input("Enter Student ID to delete: "))


    delete_query = """
    DELETE FROM students
    WHERE student_id = %s
    """


    data = (student_id,)


    cursor.execute(delete_query, data)


    connection.commit()

    print("Data deleted successfully!")
def view_data(cursor):

    select_query = """
    SELECT * FROM students
    """


    cursor.execute(select_query)


    result = cursor.fetchall()


    if result:
        print("\nStudent Data:")
        for row in result:
            print(row)
    else:
        print("\nNo data available.")

def close_connection(connection, cursor):

    cursor.close()
    connection.close()
