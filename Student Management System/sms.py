students = {}

def add_student():
   student_id = input("Enter the Student ID:")
   
   if student_id in students:
      print("Student already exists")
      return  
   
   student_name = input("Enter name:")
   try:
      age = int(input("Enter age:"))
   except ValueError:
      print("Enter a valid age")
      return
      
   course = input("Enter Course:")
   email = input("Enter Email:")
   
   students[student_id]= {
      "Student ID" : student_id,
      "Student Name": student_name,
      "Age" : age,
      "Course" : course,
      "Email": email
   }
   
   print("Student added successfully!")
   
def display_Details():
   if not students:
      print("No student records found")
      return
   
   print("\n ALL STUDENTS")
   for student in students.values():
      print(f"Student ID :  {student["Student ID"]}")
      print(f"Student Name : {student["Student Name"]}")
      print(f"Age : {student["Age"]}")
      print(f"Course : {student["Course"]}")
      print(f"Email : {student["Email"]}")
      print("---------------------------")
      
def search_Student():
   id = input("Enter an id: ")
   if id in students:
      student = students[id]
      print("===STUDENT DETAIL===")
      print(f"Student ID :  {student["Student ID"]}")
      print(f"Student Name : {student["Student Name"]}")
      print(f"Age : {student["Age"]}")
      print(f"Course : {student["Course"]}")
      print(f"Email : {student["Email"]}")
   
   else:
      print('No student found')
      
def delete_Student():
   id = input("Enter id: ")
   if id in students:
      del students[id]
      print('Student deleted')
   else:
      print('No student found')
      
while True:
   print("\n =====STUDENT MANAGEMENT SYSTEM=====")
   print("1. Add student")
   print("2. Display all students")
   print("3. Search student")
   print("4. Delete student")
   print("5. Exit")
   
   choice = int(input("Enter your choice: "))
   
   if choice == 1:
      add_student()
   elif choice == 2:
      display_Details()
   elif choice == 3:
      search_Student()
   elif choice == 4:
      delete_Student()
   elif choice == 5:
      print("Thank you ")
      break
   else:
      print("Invalid choice")