import os

class User:
    def __init__(self, username, full_name, role):
        self.username = username
        self.full_name = full_name
        self.role = role

def authenticate(username, password):
    try:
        with open("password.txt", "r") as file:
            for line in file:
                fields = line.strip().split(",")
                if len(fields) != 3:
                    continue
                stored_username, stored_password, role = fields
                if username == stored_username and password == stored_password:
                    return role
    except Exception as e:
        print(f"Auth Error: {e}")
    return None

def get_user_details(username):
    try:
        with open("user.txt", "r") as file:
            for line in file:
                stored_username, full_name, role = line.strip().split(",")
                if username == stored_username:
                    return User(username, full_name, role)
    except Exception as e:
        print(f"User Error: {e}")
    return None

def add_user(username, full_name, password, role):
    try:
        with open("user.txt", "r") as f:
            if any(line.startswith(username + ",") for line in f):
                return False
        with open("user.txt", "a") as f:
            f.write(f"{username},{full_name},{role}\n")
        with open("password.txt", "a") as f:
            f.write(f"{username},{password},{role}\n")
        return True
    except Exception as e:
        print(f"Add Error: {e}")
        return False

def delete_user(username):
    try:
        for filename in ["user.txt", "password.txt"]:
            with open(filename, "r") as f:
                lines = f.readlines()
            with open(filename, "w") as f:
                for line in lines:
                    if not line.startswith(username + ","):
                        f.write(line)
        return True
    except Exception as e:
        print(f"Delete Error: {e}")
        return False

def get_student_grades(username):
    try:
        with open("grade.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == username:
                    return parts[1:]
    except:
        pass
    return []

def get_student_eca(username):
    try:
        with open("eca.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == username:
                    return parts[1:]
    except:
        pass
    return []

def update_student_profile(username, new_full_name):
    try:
        updated = False
        with open("user.txt", "r") as f:
            lines = f.readlines()
        with open("user.txt", "w") as f:
            for line in lines:
                u, name, role = line.strip().split(",")
                if u == username:
                    f.write(f"{username},{new_full_name},{role}\n")
                    updated = True
                else:
                    f.write(line)
        return updated
    except:
        return False