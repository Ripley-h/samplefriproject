import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from sqlite3 import Error

# --- Database Functions ---

def create_connection(db_file):
    """ Create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def setup_database():
    """ Create the database and the customers table if they don't exist """
    database = "customer_data.db"

    sql_create_customers_table = """ CREATE TABLE IF NOT EXISTS customers (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        name text NOT NULL,
                                        birthday text,
                                        email text,
                                        phone_number text,
                                        address text,
                                        contact_method text
                                    ); """
    
    conn = create_connection(database)
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(sql_create_customers_table)
            conn.close()
        except Error as e:
            print(e)
    else:
        print("Error! cannot create the database connection.")

def add_customer(customer_data):
    """
    Add a new customer into the customers table
    :param customer_data: A tuple containing the customer's data
    """
    database = "customer_data.db"
    conn = create_connection(database)
    if conn:
        sql = ''' INSERT INTO customers(name,birthday,email,phone_number,address,contact_method)
                  VALUES(?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, customer_data)
        conn.commit()
        conn.close()
        return cur.lastrowid
    return None

# --- GUI Functions ---

def submit_form():
    """
    This function is called when the Submit button is clicked.
    It retrieves the data, adds it to the database, and then clears the fields.
    """
    name = name_var.get()
    birthday = birthday_var.get()
    email = email_var.get()
    phone = phone_var.get()
    address = address_var.get()
    contact_method = contact_method_var.get()
    
    # Basic validation: ensure the name field is not empty
    if not name:
        messagebox.showerror("Input Error", "Name field cannot be empty.")
        return

    customer_info = (name, birthday, email, phone, address, contact_method)
    
    # Add data to the database
    customer_id = add_customer(customer_info)

    if customer_id:
        print(f"Successfully added customer with ID: {customer_id}")
        # Use a simple dialog box for confirmation
        messagebox.showinfo("Success", "Customer information has been saved successfully!")
    else:
        print("Failed to add customer.")
        messagebox.showerror("Database Error", "Failed to save customer information.")


    # --- Clear the form fields for the next entry ---
    name_var.set("")
    birthday_var.set("")
    email_var.set("")
    phone_var.set("")
    address_var.set("")
    contact_method_var.set(contact_options[0])
    
    name_entry.focus()


# --- Main Application Window Setup ---
# Run the database setup first to ensure the table exists
setup_database()

# Create the main window
root = tk.Tk()
root.title("Customer Information Form")
root.geometry("500x350") 
root.columnconfigure(0, weight=1) 

# --- Main Frame ---
main_frame = ttk.Frame(root, padding="20 10 20 20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_frame.columnconfigure(1, weight=1)

# --- Tkinter String Variables ---
name_var = tk.StringVar()
birthday_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
address_var = tk.StringVar()
contact_method_var = tk.StringVar()

# --- Widget Creation and Layout ---

# 1. Name
name_label = ttk.Label(main_frame, text="Name:")
name_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
name_entry = ttk.Entry(main_frame, width=40, textvariable=name_var)
name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

# 2. Birthday
birthday_label = ttk.Label(main_frame, text="Birthday (YYYY-MM-DD):")
birthday_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
birthday_entry = ttk.Entry(main_frame, width=40, textvariable=birthday_var)
birthday_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

# 3. Email
email_label = ttk.Label(main_frame, text="Email:")
email_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
email_entry = ttk.Entry(main_frame, width=40, textvariable=email_var)
email_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

# 4. Phone Number
phone_label = ttk.Label(main_frame, text="Phone Number:")
phone_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
phone_entry = ttk.Entry(main_frame, width=40, textvariable=phone_var)
phone_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

# 5. Address
address_label = ttk.Label(main_frame, text="Address:")
address_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
address_entry = ttk.Entry(main_frame, width=40, textvariable=address_var)
address_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

# 6. Preferred Contact Method (Dropdown)
contact_label = ttk.Label(main_frame, text="Preferred Contact:")
contact_label.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)

contact_options = ['Email', 'Phone', 'Mail']
contact_menu = ttk.Combobox(main_frame, textvariable=contact_method_var, values=contact_options, state='readonly')
contact_menu.grid(row=5, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
contact_menu.current(0) 

# 7. Submit Button
submit_button = ttk.Button(main_frame, text="Submit", command=submit_form)
submit_button.grid(row=6, column=0, columnspan=2, pady=20) 

name_entry.focus()

# --- Start the Main Event Loop ---
root.mainloop()
