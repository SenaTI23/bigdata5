import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['TokoOnline']
collection = db['products']

# Function to add product
def add_product():
    name = entry_name.get()
    category = entry_category.get()
    
    if not name or not category:
        messagebox.showerror("Error", "Please enter both name and category.")
        return
    
    product = {"name": name, "category": category}
    collection.insert_one(product)
    messagebox.showinfo("Success", "Product added successfully!")

# Function to show products
def show_products():
    products = collection.find()
    product_list = ""
    for product in products:
        product_list += f"Name: {product['name']}, Category: {product['category']}\n"
    
    if not product_list:
        product_list = "No products found."
        
    messagebox.showinfo("Products in Database", product_list)

# GUI setup
root = tk.Tk()
root.title("Add Product")

tk.Label(root, text="Product Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Category").pack()
entry_category = tk.Entry(root)
entry_category.pack()

tk.Button(root, text="Add Product", command=add_product).pack()
tk.Button(root, text="Show Products", command=show_products).pack()

root.mainloop()
