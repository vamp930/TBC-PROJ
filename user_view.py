import tkinter as tk
from tkinter import messagebox
from auth import *

root = tk.Tk()
root.title("SPMS")
root.geometry("400x300")

main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill="both")

def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

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
    clear_frame()
    tk.Label(main_frame, text=f"Welcome {user.full_name}").pack(pady=10)
    
    def add_ui():
        clear_frame()
        tk.Label(main_frame, text="Add User").pack()
        tk.Label(main_frame, text="Username").pack()
        u_entry = tk.Entry(main_frame)
        u_entry.pack()
        tk.Label(main_frame, text="Full Name").pack()
        f_entry = tk.Entry(main_frame)
        f_entry.pack()
        tk.Label(main_frame, text="Password").pack()
        p_entry = tk.Entry(main_frame, show="*")
        p_entry.pack()
        role_var = tk.StringVar(value="student")
        tk.OptionMenu(main_frame, role_var, "admin", "student").pack()
        def submit():
            if add_user(u_entry.get(), f_entry.get(), p_entry.get(), role_var.get()):
                messagebox.showinfo("Success", "User added!")
                admin_dashboard(user)
            else:
                messagebox.showerror("Failed", "User already exists.")
        tk.Button(main_frame, text="Submit", command=submit).pack()
        tk.Button(main_frame, text="Back", command=lambda: admin_dashboard(user)).pack(pady=5)

    def delete_ui():
        clear_frame()
        tk.Label(main_frame, text="Delete User").pack()
        entry = tk.Entry(main_frame)
        entry.pack()
        def submit():
            if delete_user(entry.get()):
                messagebox.showinfo("Deleted", "User deleted.")
                admin_dashboard(user)
            else:
                messagebox.showerror("Error", "User not found.")
        tk.Button(main_frame, text="Delete", command=submit).pack()
        tk.Button(main_frame, text="Back", command=lambda: admin_dashboard(user)).pack(pady=5)

    tk.Button(main_frame, text="Add User", command=add_ui).pack(pady=5)
    tk.Button(main_frame, text="Delete User", command=delete_ui).pack(pady=5)

def student_dashboard(user):
    clear_frame()
    tk.Label(main_frame, text=f"Welcome {user.full_name}").pack()

    def view_info():
        clear_frame()
        grades = get_student_grades(user.username)
        eca = get_student_eca(user.username)
        tk.Label(main_frame, text=f"Name: {user.full_name}").pack()
        tk.Label(main_frame, text="Grades:").pack()
        for g in grades:
            tk.Label(main_frame, text=f"- {g}").pack()
        tk.Label(main_frame, text="ECA:").pack()
        for act in eca:
            tk.Label(main_frame, text=f"- {act}").pack()
        tk.Button(main_frame, text="Back", command=lambda: student_dashboard(user)).pack(pady=5)

    def update_info():
        clear_frame()
        tk.Label(main_frame, text="Update Profile").pack()
        name_entry = tk.Entry(main_frame)
        name_entry.insert(0, user.full_name)
        name_entry.pack()
        def submit():
            if update_student_profile(user.username, name_entry.get()):
                messagebox.showinfo("Updated", "Profile updated.")
                user.full_name = name_entry.get()
                student_dashboard(user)
        tk.Button(main_frame, text="Submit", command=submit).pack()
        tk.Button(main_frame, text="Back", command=lambda: student_dashboard(user)).pack(pady=5)

    tk.Button(main_frame, text="View Info", command=view_info).pack(pady=5)
    tk.Button(main_frame, text="Update Info", command=update_info).pack(pady=5)

def show_login():
    clear_frame()
    global username_entry, password_entry
    tk.Label(main_frame, text="Username").pack(pady=5)
    username_entry = tk.Entry(main_frame)
    username_entry.pack(pady=5)
    tk.Label(main_frame, text="Password").pack(pady=5)
    password_entry = tk.Entry(main_frame, show="*")
    password_entry.pack(pady=5)
    tk.Button(main_frame, text="Login", command=login).pack(pady=10)

if __name__ == "__main__":
    show_login()
    root.mainloop()
