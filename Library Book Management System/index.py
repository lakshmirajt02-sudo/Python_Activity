books = {}

def add_Books():
   book_id = input("Enter the book id: ")
   if book_id in books:
      print("Book is already present")
      return
   book_name = input("Enter name of the book: ")
   author = input("Enter author: ")
   category = input("Enter category: ")
   
   try:
      price = int(input("Enter the book price: "))
   except ValueError:
      print("Enter valid price")
      return
   
   books[book_id]= {
      "book id" : book_id,
      "book name" : book_name,
      "author" : author,
      "category" : category,
      "price" : price 
   }
   print("Book added Successfullt")
   
def display_Books():
   print("\n===Book Details===")
   if not books:
      print("No book record")
      return
   for book in books.values():
      print(f"Book Id : {book["book id"]}")
      print(f"Book Name : {book["book name"]}")
      print(f"Author : {book["author"]}")
      print(f"Category : {book["category"]}")
      print(f"Price: {book["price"]}")
      print("======================")
      
def search_Book():
   id = input("Enter book id: ")
   if id in books:
      book = books[id]
      print("Book Detail")
      print(f"Book Id : {book["book id"]}")
      print(f"Book Name : {book["book name"]}")
      print(f"Author : {book["author"]}")
      print(f"Category : {book["category"]}")
      print(f"Price: {book["price"]}")
   else:
      print("No book found")
      
def delete_Book():
   id = input("Enter book id: ")
   if id in books:
      del books[id]
      print("Book deleted")
   else:
      print("No books found")
      
while True:
   print("=== LIBRARY BOOK MANAGEMENT SYSTEM ===")
   print("1. Add Book")
   print("2. Display All Books")
   print("3. Search Book")
   print("4. Delete Book")
   print("5. Exit")
   
   choice = int(input("Enter your choice: "))
   
   if choice == 1:
      add_Books()
   elif choice == 2:
      display_Books()
   elif choice == 3:
      search_Book()
   elif choice == 4:
      delete_Book()
   elif choice == 5:
      print("Thank You")
      break
   else:
      print("Invalid choice")
      
      
      
   