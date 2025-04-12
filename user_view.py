import tkinter as tk
from tkinter import messagebox
from auth import *

def login():
    username = username_entry.get()
    password = password_entry.get()
    role = authenticate(username, password)

    if role:
        user = get_user_details(username)
        if role == "admin":
            admin_dashboard(user)
        elif role == "student":
            student_dashboard(user)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def admin_dashboard(user):
    def add_ui():
        def submit():
            u = u_entry.get()
            f = f_entry.get()
            p = p_entry.get()
            r = role_var.get()
            if add_user(u, f, p, r):
                messagebox.showinfo("Success", "User added!")
                win.destroy()
            else:
                messagebox.showerror("Failed", "User already exists.")
        win = tk.Toplevel()
        win.title("Add User")
        tk.Label(win, text="Username").pack()
        u_entry = tk.Entry(win)
        u_entry.pack()
        tk.Label(win, text="Full Name").pack()
        f_entry = tk.Entry(win)
        f_entry.pack()
        tk.Label(win, text="Password").pack()
        p_entry = tk.Entry(win, show="*")
        p_entry.pack()
        role_var = tk.StringVar(value="student")
        tk.OptionMenu(win, role_var, "admin", "student").pack()
        tk.Button(win, text="Submit", command=submit).pack()

    def delete_ui():
        def submit():
            u = entry.get()
            if delete_user(u):
                messagebox.showinfo("Deleted", "User deleted.")
                win.destroy()
            else:
                messagebox.showerror("Error", "User not found.")
        win = tk.Toplevel()
        win.title("Delete User")
        tk.Label(win, text="Username").pack()
        entry = tk.Entry(win)
        entry.pack()
        tk.Button(win, text="Delete", command=submit).pack()

    win = tk.Toplevel()
    win.title("Admin Dashboard")
    tk.Label(win, text=f"Welcome {user.full_name}").pack(pady=10)
    tk.Button(win, text="Add User", command=add_ui).pack(pady=5)
    tk.Button(win, text="Delete User", command=delete_ui).pack(pady=5)

def student_dashboard(user):
    def view_info():
        grades = get_student_grades(user.username)
        eca = get_student_eca(user.username)
        win = tk.Toplevel()
        win.title("Student Info")
        tk.Label(win, text=f"Name: {user.full_name}").pack()
        tk.Label(win, text="Grades:").pack()
        for g in grades:
            tk.Label(win, text=f"- {g}").pack()
        tk.Label(win, text="ECA:").pack()
        for act in eca:
            tk.Label(win, text=f"- {act}").pack()

    def update_info():
        def submit():
            new_name = name_entry.get()
            if update_student_profile(user.username, new_name):
                messagebox.showinfo("Updated", "Profile updated.")
                win.destroy()
        win = tk.Toplevel()
        win.title("Update Info")
        tk.Label(win, text="New Full Name").pack()
        name_entry = tk.Entry(win)
        name_entry.insert(0, user.full_name)
        name_entry.pack()
        tk.Button(win, text="Submit", command=submit).pack()

    win = tk.Toplevel()
    win.title("Student Dashboard")
    tk.Label(win, text=f"Welcome {user.full_name}").pack()
    tk.Button(win, text="View Info", command=view_info).pack()
    tk.Button(win, text="Update Info", command=update_info).pack()

def main():
    global username_entry, password_entry
    root = tk.Tk()
    root.title("SPMS Login")
    root.geometry("300x250")
    frame = tk.Frame(root)
    frame.pack(expand=True)
    tk.Label(frame, text="Username").pack(pady=5)
    username_entry = tk.Entry(frame)
    username_entry.pack(pady=5)
    tk.Label(frame, text="Password").pack(pady=5)
    password_entry = tk.Entry(frame, show="*")
    password_entry.pack(pady=5)
    tk.Button(frame, text="Login", command=login).pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    main()
# This code is a simple GUI application for a Student Profile Management System (SPMS).
# It allows users to log in as either an admin or a student and provides different functionalities based on the role.
# The admin can add or delete users, while the student can view and update their information.
# The application uses the Tkinter library for the GUI and includes functions for user authentication,
# user management, and data retrieval from text files.