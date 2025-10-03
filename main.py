import tkinter as tk
from tkinter import ttk # ttk gives access to modern-looking "themed widgets"

# --- Functions ---
def submit_form():
    """
    This function is called when the Submit button is clicked.
    It retrieves the data, prints it, and then clears the fields.
    """
    # Use the .get() method to retrieve the current value from each StringVar
    name = name_var.get()
    birthday = birthday_var.get()
    email = email_var.get()
    phone = phone_var.get()
    address = address_var.get()
    contact_method = contact_method_var.get()
    
    # Print the collected information to the console
    print("\n--- Customer Information Submitted ---")
    print(f"Customer Name: {name}")
    print(f"Birthday: {birthday}")
    print(f"Email: {email}")
    print(f"Phone Number: {phone}")
    print(f"Address: {address}")
    print(f"Preferred Contact Method: {contact_method}")
    print("------------------------------------\n")

    # --- NEW: Clear the form fields for the next entry ---
    # Use the .set() method to change the value of the StringVars
    name_var.set("")
    birthday_var.set("")
    email_var.set("")
    phone_var.set("")
    address_var.set("")
    
    # Reset the dropdown menu to the first option
    contact_method_var.set(contact_options[0])
    
    # Set focus back to the first entry field for convenience
    name_entry.focus()


# --- Main Application Window Setup ---
# Create the main window
root = tk.Tk()
root.title("Customer Information Form")
root.geometry("500x350") # Set a default size for the window
root.columnconfigure(0, weight=1) # Allow the main column to expand

# --- Main Frame ---
# It's good practice to put all widgets in a frame
main_frame = ttk.Frame(root, padding="20 10 20 20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_frame.columnconfigure(1, weight=1) # Allow the entry field column to expand

# --- Tkinter String Variables ---
# These variables will be linked to the widgets to easily get/set their values
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
contact_menu.current(0) # Set the default selection to the first item ('Email')

# 7. Submit Button
# The `command` option is linked to the submit_form function
submit_button = ttk.Button(main_frame, text="Submit", command=submit_form)
submit_button.grid(row=6, column=0, columnspan=2, pady=20) # columnspan=2 makes it span both columns

# Place the focus on the first entry field when the app starts
name_entry.focus()

# --- Start the Main Event Loop ---
# This line displays the window and waits for user interaction
root.mainloop()