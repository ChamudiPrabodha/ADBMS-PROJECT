import tkinter as tk
from tkinter import ttk, messagebox
from db import add_item, fetch_items, add_customer, fetch_customers

root = tk.Tk()
root.title("Weerakkodi Super Store Management")

# Create notebook (tabs)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Create frames for each tab
item_frame = ttk.Frame(notebook, width=600, height=400)
customer_frame = ttk.Frame(notebook, width=600, height=400)

item_frame.pack(fill='both', expand=True)
customer_frame.pack(fill='both', expand=True)

# Add frames as tabs
notebook.add(item_frame, text='Item Management')
notebook.add(customer_frame, text='Customer Management')


### --- ITEM TAB --- ###
def submit_item():
    ItemID = entry_id.get()
    Itemname = entry_name.get()
    Price = entry_price.get()
    Category = entry_category.get()
    Stockqty = entry_stock.get()
    ManagerID = entry_manager.get()

    if not all([ItemID, Itemname, Price, Category, Stockqty, ManagerID]):
        messagebox.showwarning("Validation Error", "All fields are required")
        return

    try:
        float(Price)
        int(Stockqty)
    except ValueError:
        messagebox.showerror("Input Error", "Price must be a number and Stock Qty must be an integer.")
        return

    add_item(ItemID, Itemname, float(Price), Category, int(Stockqty), ManagerID)
    messagebox.showinfo("Success", "Item added successfully")
    clear_item_entries()

def show_items():
    items = fetch_items()
    output_item.delete(1.0, tk.END)
    for i in items:
        output_item.insert(tk.END, f"{i[0]} | {i[1]} | {i[2]} | {i[3]} | {i[4]} | {i[5]}\n")

def clear_item_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_stock.delete(0, tk.END)
    entry_manager.delete(0, tk.END)

# Item widgets
tk.Label(item_frame, text="Item ID").grid(row=0, column=0)
entry_id = tk.Entry(item_frame)
entry_id.grid(row=0, column=1)

tk.Label(item_frame, text="Item Name").grid(row=1, column=0)
entry_name = tk.Entry(item_frame)
entry_name.grid(row=1, column=1)

tk.Label(item_frame, text="Price").grid(row=2, column=0)
entry_price = tk.Entry(item_frame)
entry_price.grid(row=2, column=1)

tk.Label(item_frame, text="Category").grid(row=3, column=0)
entry_category = tk.Entry(item_frame)
entry_category.grid(row=3, column=1)

tk.Label(item_frame, text="Stock Quantity").grid(row=4, column=0)
entry_stock = tk.Entry(item_frame)
entry_stock.grid(row=4, column=1)

tk.Label(item_frame, text="Manager ID").grid(row=5, column=0)
entry_manager = tk.Entry(item_frame)
entry_manager.grid(row=5, column=1)

tk.Button(item_frame, text="Add Item", command=submit_item).grid(row=6, column=0, columnspan=2, pady=10)
tk.Button(item_frame, text="Show Items", command=show_items).grid(row=7, column=0, columnspan=2)

output_item = tk.Text(item_frame, height=10, width=70)
output_item.grid(row=8, column=0, columnspan=2, pady=10)


### --- CUSTOMER TAB --- ###
def submit_customer():
    cid = entry_cid.get()
    name = entry_cname.get()
    contact = entry_ccontact.get()

    if not cid or not name or not contact:
        messagebox.showwarning("Validation Error", "All fields are required")
        return

    add_customer(cid, name, contact)
    messagebox.showinfo("Success", "Customer added successfully")
    entry_cid.delete(0, tk.END)
    entry_cname.delete(0, tk.END)
    entry_ccontact.delete(0, tk.END)

def show_customers():
    customers = fetch_customers()
    output_customer.delete(1.0, tk.END)
    for c in customers:
        output_customer.insert(tk.END, f"{c[0]} | {c[1]} | {c[2]}\n")

# Customer widgets
tk.Label(customer_frame, text="Customer ID").grid(row=0, column=0)
entry_cid = tk.Entry(customer_frame)
entry_cid.grid(row=0, column=1)

tk.Label(customer_frame, text="Name").grid(row=1, column=0)
entry_cname = tk.Entry(customer_frame)
entry_cname.grid(row=1, column=1)

tk.Label(customer_frame, text="Contact Info").grid(row=2, column=0)
entry_ccontact = tk.Entry(customer_frame)
entry_ccontact.grid(row=2, column=1)

tk.Button(customer_frame, text="Add Customer", command=submit_customer).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(customer_frame, text="Show Customers", command=show_customers).grid(row=4, column=0, columnspan=2)

output_customer = tk.Text(customer_frame, height=10, width=70)
output_customer.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

