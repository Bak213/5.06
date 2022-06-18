import sqlite3
from typing import Union
# 1). Create a database
connection = sqlite3.connect("app.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students (name text, age real)")
connection.commit()
connection.close()

# 2). Create models
class Student:
    def __init__(self, name:str, age:int | float):
        self.name =name
        self.age = age
    
"""
3). CRUD methods
(C)reate
(R)ead
(U)update
(D)elete
"""

def create_student(name, age: int | float, connection: sqlite3.Connection):
    new_student = Student(name, age)
    cursor = connection.cursor()
    #cursor.execute(f"INSERT INTO students VALUES ({new_student}, {new_student.age})")
    cursor.execute("INSERT INTO students VALUES (?, ?)", (new_student.name, new_student.age))
    connection.commit()
    

def read_students(connection: sqlite3.Connection) -> list[Student]:
    cursor = connection.cursor()
    queryset = cursor.execute("SELECT * FROM students").fetchall()
    students = []
    for result in queryset: 
        student=Student(result[0], result[1])
        students.append(student)
    return students


def delete_student(name: str, connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE name=?", (name,))
    connection.commit()

def update_student(name: str,name2: str, age2: int, connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.execute("UPDATE students SET name=? WHERE name=?", (name2, name,))
    cursor.execute("UPDATE students SET age=? WHERE name=?", (age2, name,))
    connection.commit()
    

    
# 4). Create UI
print("wahat would youn like to do?")
print("0. Exit")
print("1. Create new student")
print("2. Read students")
print("3. Delete students")
print("4. Update students")
option = input("Please specify an option: ")

if option == '0':
    exit()
elif option == '1':
    name = input("Please specify students name:")
    age = input("Please specify students age: ")
    connection = sqlite3.connect("app.db")
    create_student(name, age, connection)
    connection.close()
elif option == '2':
    connection= sqlite3.connect("app.db")
    students = read_students(connection)
    connection.close()
    print(students)
    
    for student in students:
        print(student)
        
elif option == '3':
    name = input("Please specify students name:")
    connection = sqlite3.connect("app.db")
    delete_student(name, connection)
    connection.close()
    
elif option == '4':
    name = input("Please specify students name:")
    name2 = input("Please specify new name:")
    age2 = input("Please specify new age:")
    connection = sqlite3.connect("app.db")
    update_student(name, name2, age2, connection)
    connection.close()
   
    
   