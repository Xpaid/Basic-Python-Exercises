import os
import sys

if os.environ.get("RUNNING_FROM_MAIN") != "true":
    print("Unauthorized access detected!")
    sys.exit()

import tkinter as tk
import subprocess
from resources import *

USER_CREDENTIALS = {
    "jetro": "pass",
}

def open_home():
    uname = username.get().strip()
    passwd = password.get().strip()
    
    if uname and passwd: 
        if USER_CREDENTIALS.get(uname) == passwd: 
            x, y = root.winfo_x(), root.winfo_y()
            subprocess.Popen([sys.executable, "src/home.py", uname, str(x), str(y)])  # Open home page and pass position
            root.destroy()
        else:
            error_label.config(text="Invalid username or password", fg="#dc3545")
    else:
        error_label.config(text="Please enter both username and password", fg="#dc3545")

# Create the main window
root = tk.Tk()

# Check if position arguments are passed from the home page
if len(sys.argv) > 2:
    x, y = int(sys.argv[1]), int(sys.argv[2])
else:
    x, y = 100, 100  # Default position if no args

root.geometry(f"900x600+{x}+{y}")  # Set position from passed args
root.title("Login")
root.configure(bg=DARK)
root.resizable(False, False)

# Label for "Login"
lgnLabel = tk.Label(
    root, text="Login", 
    font=(Bloxat, 75, "bold"),  # Use Bloxat font
    fg=WARNING,
    bg=DARK
)
lgnLabel.pack(pady=80)

# Username Entry
username = tk.Entry(root, font=(Bloxat, 14), bg=DARK, fg=LIGHT, bd=0, relief="flat", insertbackground="white", justify="center")
username.pack(pady=(0, 0), ipadx=10, ipady=5)

# Add a line below the username entry
username_line = tk.Canvas(root, height=2, width=200, bg=DARK, bd=0, highlightthickness=0)
username_line.create_line(0, 1, 200, 1, fill=LIGHT)
username_line.pack(pady=(0, 10))

# Username Label (Now below the line)
username_label = tk.Label(root, text="Username", font=(Bloxat, 10), fg=SECONDARY, bg=DARK)
username_label.pack(pady=5)

# Password Entry
password = tk.Entry(root, font=(Bloxat, 14), bg=DARK, fg=LIGHT, bd=0, relief="flat", show="*", insertbackground="white", justify="center")
password.pack(pady=(0, 0), ipadx=10, ipady=10)

# Add a line below the password entry
password_line = tk.Canvas(root, height=2, width=200, bg=DARK, bd=0, highlightthickness=0)
password_line.create_line(0, 1, 200, 1, fill=LIGHT)
password_line.pack(pady=(0, 10))

# Password Label (Now below the line)
password_label = tk.Label(root, text="Password", font=(Bloxat, 10), fg=SECONDARY, bg=DARK)
password_label.pack(pady=5)

# Error message label (if any)
error_label = tk.Label(root, text="", font=(Bloxat, 12), fg="#dc3545", bg=DARK)
error_label.pack(pady=(10, 0))

# Login Button
login_button = tk.Button(
    root, text="Go", 
    font=(Bloxat, 14),
    fg=LIGHT, 
    bg=SUCCESS, 
    relief="raised",
    padx=20, pady=10,
    width=10, height=1,
    bd=7, 
    highlightthickness=0,
    command=open_home
)
login_button.pack(pady=30)

# Run the application
root.mainloop()
