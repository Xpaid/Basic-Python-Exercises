import tkinter as tk
import subprocess
import sys
from resources import *  

def go_back(uname, x, y, root):
    current_x = root.winfo_x()
    current_y = root.winfo_y()
    
    root.destroy()  
    subprocess.Popen([sys.executable, "src/home.py", uname, str(current_x), str(current_y)]) 

def reverse_name(entry, result_label):
    name = entry.get()
    reversed_name = name[::-1]
    result_label.config(text=f"Reversed: {reversed_name}", fg=INFO)

def init(uname, x, y):
    root = tk.Tk()
    root.geometry("900x600")
    root.title("Reverse Name")
    root.configure(bg=DARK)
    root.resizable(False, False)
    root.geometry(f"900x600+{x}+{y}")

    back_button = tk.Button(root, text="Back to Home", command=lambda: go_back(uname, x, y, root),
                            font=("Bloxat", 12), fg=DARK, bg=WARNING, relief="flat")
    back_button.place(x=20, y=20)

    title = tk.Label(root, text="Reverse Your Name", font=("Bloxat", 20), fg=WARNING, bg=DARK)
    title.pack(pady=60)

    label = tk.Label(root, text="Enter your name below", font=("Bloxat", 14), fg=LIGHT, bg=DARK)
    label.pack(pady=10)

    name_entry = tk.Entry(root, font=("Bloxat", 14), fg=LIGHT, bg=DARK, bd=0, relief="flat", 
                          insertbackground=LIGHT, justify="center", width=30)
    name_entry.pack(pady=10)
    name_entry.config(highlightthickness=2, highlightbackground=PRIMARY, highlightcolor=PRIMARY)

    result_label = tk.Label(root, text="", font=("Bloxat", 14), fg=INFO, bg=DARK)
    result_label.pack(pady=10)

    reverse_btn = tk.Button(root, text="Reverse Name", font=("Bloxat", 14), fg=LIGHT, bg=SUCCESS,
                            relief="flat", command=lambda: reverse_name(name_entry, result_label))
    reverse_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 3:  
        username = sys.argv[1]
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        init(username, x, y)
    else:
        print("Missing arguments for username or window position.")
