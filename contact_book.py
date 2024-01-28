import tkinter as tk
from tkinter import messagebox

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contact_list.insert(tk.END, f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}")
        clear_entries()
    else:
        messagebox.showwarning("Error", "Please enter at least name and phone number.")

def search_contact():
    search_term = search_entry.get().lower()
    contact_list.delete(0, tk.END)  

    for contact in contacts:
        if search_term in contact.lower():
            contact_list.insert(tk.END, contact)

def delete_contact():
    try:
        selected_index = contact_list.curselection()[0]
        contact_list.delete(selected_index)
    except IndexError:
        pass


def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

contacts = []

root = tk.Tk()
root.title("Contact Management System")

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()
search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

contact_list = tk.Listbox(root)
contact_list.pack()

root.mainloop()
