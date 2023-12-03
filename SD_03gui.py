import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, master):
        self.master = master
        self.contacts = {}
        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.master, text="Name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack()

        self.phone_label = tk.Label(self.master, text="Phone:")
        self.phone_label.pack()

        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.pack()

        self.email_label = tk.Label(self.master, text="Email:")
        self.email_label.pack()

        self.email_entry = tk.Entry(self.master)
        self.email_entry.pack()

        self.add_button = tk.Button(self.master, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        self.view_button = tk.Button(self.master, text="View Contacts", command=self.view_contacts)
        self.view_button.pack()

        self.edit_button = tk.Button(self.master, text="Edit Contact", command=self.edit_contact)
        self.edit_button.pack()

        self.delete_button = tk.Button(self.master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if not name:
            messagebox.showinfo("Contact Manager", "Please enter a name.")
            return

        if not phone:
            messagebox.showinfo("Contact Manager", "Please enter a phone number.")
            return

        if not email:
            messagebox.showinfo("Contact Manager", "Please enter an email address.")
            return

        if name in self.contacts:
            messagebox.showinfo("Contact Manager", f"Contact '{name}' already exists. Please edit or delete the existing contact.")
        else:
            self.contacts[name] = {"Phone": phone, "Email": email}
            messagebox.showinfo("Contact Manager", f"Contact '{name}' added successfully!")
    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Contact Manager", "No contacts found.")
        else:
            message = ""
            for name, info in self.contacts.items():
                message += f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}\n"
            messagebox.showinfo("Contact Manager", message)
    def edit_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            messagebox.showinfo("Contact Manager", f"Editing contact: {name}")
            phone = self.phone_entry.get()
            email = self.email_entry.get()

            if not phone:
                messagebox.showinfo("Contact Manager", "Please enter a phone number.")
                return

            if not email:
                messagebox.showinfo("Contact Manager", "Please enter an email address.")
                return

            self.contacts[name]["Phone"] = phone
            self.contacts[name]["Email"] = email
            messagebox.showinfo("Contact Manager", f"Contact '{name}' edited successfully!")
        else:
            messagebox.showinfo("Contact Manager", f"Contact '{name}' not found.")
    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Contact Manager", f"Contact '{name}' deleted successfully!")
        else:
            messagebox.showinfo("Contact Manager", f"Contact '{name}' not found.")

root = tk.Tk()
root.title("Contact Manager")
app = ContactManager(root)
root.mainloop()