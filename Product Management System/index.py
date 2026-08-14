products = {}

def add_Product():
   product_id = input("Enter the product id: ")
   
   if product_id in products:
      print("This product already present")
      return
   product_name = input("Enter product name: ")
   category = input("Enter category: ")
   
   try:
      price = int(input("Enter the price: "))
   except ValueError:
      print("Write valid price")
      return
      
   try:
      stock_quantity = int(input("Enter the quantity: "))
   except ValueError:
      print("No valid stock")
      return
   
   products[product_id] = {
      "Product_Id" : product_id,
      "Product_Name" : product_name,
      "Category" : category,
      "Price" : price,
      "Stock Quantity": stock_quantity
   }
   
   print("Product added successfully")
   
def display_Products():
   print("\n ===PRODUCT DETAILS===")
   if not products:
      print("No product records")
   for product in products.values():
      print(f"Product ID : {product["Product_Id"]}")
      print(f"Product Name : {product["Product_Name"]}")
      print(f"Category : {product["Category"]}")
      print(f"Price : {product["Price"]}")
      print(f"Stock Quantity : {product["Stock Quantity"]}")
      print("----------------------------")
      
def search_Products():
   product_id = input("Enter id: ")
   if product_id in products:
      product = products[product_id]
      print("\n ===Product Detail===")
      print(f"Product ID : {product["Product_Id"]}")
      print(f"Product Name : {product["Product_Name"]}")
      print(f"Category : {product["Category"]}")
      print(f"Price : {product["Price"]}")
      print(f"Stock Quantity : {product["Stock Quantity"]}")
      
   else:
      print("No product")
      
def delete_Product():
   id = input("Enter Id: ")
   if id in products:
      del products[id]
      print("product deleted")
   else:
      print("No product in that id")
      
# Menu 
while True:
   print("\n === PRODUCT MANAGEMENT SYSTEM ===")
   print("1. Add Product")
   print("2. Display All Products")
   print("3. Search Product")
   print("4. Delete Product")
   print("5. Exit")
   
   choice = input("Enter your choice : ")
   
   if choice == "1":
      add_Product()
   elif choice == "2":
      display_Products()
   elif choice == "3":
      search_Products()
   elif choice == "4":
      delete_Product()
   elif choice == "5":
      print("Thank you")
      break
   else:
      print("Invalid choice")
      
            
   
      
      
      
   