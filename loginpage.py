from tkinter import *
from tkinter import messagebox
import os
import subprocess
USER_FILE = "users.txt"

def save_user(username, password):
    with open(USER_FILE, "a") as f:
        f.write(f"{username},{password}\n")

def load_users():
    users = {}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            for line in f:
                if "," in line:
                    user, pwd = line.strip().split(",", 1)
                    users[user] = pwd
    return users


# ---------------- MAIN LOGIN WINDOW ---------------- #
root = Tk()
root.title("SWASTHYA - Login")
root.configure(bg="#d6f5f5")

root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

# Title
lb1 = Label(root, text="SWASTHYA LOGIN",
            font=("Times New Roman", 40, "bold"),
            bg="#d6f5f5", fg="#004d4d")
lb1.pack(pady=50)

# Frame for login inputs
frame = Frame(root, bg="white", bd=3, relief=SOLID, padx=30, pady=30)
frame.place(relx=0.5, rely=0.4, anchor=CENTER)
Label(frame, text="Username", font=("Arial", 14, "bold"), bg="white").grid(row=0, column=0, sticky="w", pady=10, padx=10)
e1 = Entry(frame, width=30, font=("Arial", 12))
e1.grid(row=0, column=1, pady=10, padx=10)

Label(frame, text="Password", font=("Arial", 14, "bold"), bg="white").grid(row=1, column=0, sticky="w", pady=10, padx=10)
e2 = Entry(frame, width=30, font=("Arial", 12), show="*")
e2.grid(row=1, column=1, pady=10, padx=10)


# ---------------- LOGIN FUNCTION ---------------- #
def login():
    username = e1.get()
    password = e2.get()
    users = load_users()

    if username.strip() == "" or password.strip() == "":
        messagebox.showwarning("Input Error", "Please enter Username and Password")
    elif username in users and users[username] == password:
        messagebox.showinfo("Success", f"Welcome {username}!\nLogin Successful ")
        root.destroy()  # Close login window
        subprocess.Popen(["python", "newmain.py"])  
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password ")



# ---------------- SIGNUP FUNCTION ---------------- #
def signup():
    signup_win = Toplevel(root)
    signup_win.title("SWASTHYA - Sign Up")
    signup_win.configure(bg="#e6f7ff")
    # Make signup page full screen
    signup_win.attributes("-fullscreen", True)
    signup_win.bind("<Escape>", lambda e: signup_win.attributes("-fullscreen", False))

    Label(signup_win, text="Create Your Account",
          font=("Arial", 32, "bold"),
          bg="#e6f7ff", fg="#004466").pack(pady=40)

    frame2 = Frame(signup_win, bg="white", bd=2, relief=SOLID, padx=25, pady=25)
    frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(frame2, text="Full Name", font=("Arial", 14, "bold"), bg="white").grid(row=0, column=0, sticky="w", pady=10, padx=10)
    name_entry = Entry(frame2, width=30, font=("Arial", 12)); name_entry.grid(row=0, column=1, pady=10, padx=10)

    Label(frame2, text="Email", font=("Arial", 14, "bold"), bg="white").grid(row=1, column=0, sticky="w", pady=10, padx=10)
    email_entry = Entry(frame2, width=30, font=("Arial", 12)); email_entry.grid(row=1, column=1, pady=10, padx=10)

    Label(frame2, text="Username", font=("Arial", 14, "bold"), bg="white").grid(row=2, column=0, sticky="w", pady=10, padx=10)
    user_entry = Entry(frame2, width=30, font=("Arial", 12)); user_entry.grid(row=2, column=1, pady=10, padx=10)

    Label(frame2, text="Password", font=("Arial", 14, "bold"), bg="white").grid(row=3, column=0, sticky="w", pady=10, padx=10)
    pass_entry = Entry(frame2, width=30, font=("Arial", 12), show="*"); pass_entry.grid(row=3, column=1, pady=10, padx=10)

    Label(frame2, text="Confirm Password", font=("Arial", 14, "bold"), bg="white").grid(row=4, column=0, sticky="w", pady=10, padx=10)
    conf_entry = Entry(frame2, width=30, font=("Arial", 12), show="*"); conf_entry.grid(row=4, column=1, pady=10, padx=10)

    # Register function
    def register():
        name = name_entry.get()
        email = email_entry.get()
        user = user_entry.get()
        pwd = pass_entry.get()
        conf = conf_entry.get()

        if not name or not email or not user or not pwd or not conf:
            messagebox.showwarning("Input Error", "All fields are required!", parent=signup_win)
        elif pwd != conf:
            messagebox.showerror("Password Error", "Passwords do not match ", parent=signup_win)
        else:
            users = load_users()
            if user in users:
                messagebox.showerror("Error", "Username already exists ", parent=signup_win)
            else:
                save_user(user, pwd)
                messagebox.showinfo("Success", f"Account created successfully s\nPlease login now.", parent=signup_win)
                signup_win.destroy()
                root.deiconify()  # Show login page again

    Button(signup_win, text="Sign Up", font=("Arial", 14, "bold"),
           bg="#00b3b3", fg="white", padx=20, pady=8, relief=RAISED, command=register).pack(pady=20)


# ---------------- BUTTONS ---------------- #
btn_frame = Frame(root, bg="#d6f5f5")
btn_frame.place(relx=0.5, rely=0.65, anchor=CENTER)

btn_login = Button(btn_frame, text="Login", font=("Arial", 14, "bold"),
                   bg="#006666", fg="white", padx=20, pady=8, relief=RAISED, command=login)
btn_login.pack(pady=10)

Button(btn_frame, text="Forgot Password?", font=("Arial", 12, "underline"),
       bg="#d6f5f5", fg="blue", bd=0, cursor="hand2",
       command=lambda: messagebox.showinfo("Forgot Password", "Password reset link sent!")).pack(pady=5)

Label(btn_frame, text="---------------- or ----------------", bg="#d6f5f5", fg="gray", font=("Arial", 12)).pack(pady=5)

Button(btn_frame, text="Sign Up", font=("Arial", 13, "bold"),
       bg="#00b3b3", fg="white", padx=20, pady=8, relief=RAISED, command=signup).pack(pady=10)

root.mainloop()
