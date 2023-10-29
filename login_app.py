import tkinter as tk
from tkinter import messagebox

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x150')
        self.title('Tkinter Login Form - pythonexamples.org')
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        usernameLabel = tk.Label(self, text="User Name")
        usernameLabel.grid(row=0, column=0)
        usernameEntry = tk.Entry(self, textvariable=self.username)
        usernameEntry.grid(row=0, column=1)

        passwordLabel = tk.Label(self, text="Password")
        passwordLabel.grid(row=1, column=0)
        passwordEntry = tk.Entry(self, textvariable=self.password, show='*')
        passwordEntry.grid(row=1, column=1)

        loginButton = tk.Button(self, text="Login", command=self.validateLogin)
        loginButton.grid(row=4, column=0)

    def validateLogin(self):
        username = self.username.get()
        password = self.password.get()

        # Validate the login credentials here
        if username == "admin" and password == "password":
            # Login successful
            self.destroy()
            # Open the main application window
            MainWindow().mainloop()
        else:
            # Login failed
            messagebox.showerror("Login Failed", "Invalid username or password")

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x150')
        self.title('Main Application Window - pythonexamples.org')
        # Add your main application code here

if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()
