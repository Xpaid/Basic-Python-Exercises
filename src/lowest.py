import tkinter as tk
import subprocess
import sys
from resources import *  

def go_back(uname, x, y, root):
    current_x = root.winfo_x()
    current_y = root.winfo_y()
    
    root.destroy()  
    subprocess.Popen([sys.executable, "src/home.py", uname, str(current_x), str(current_y)]) 

def find_lowest(num1_entry, num2_entry, num3_entry, num4_entry, result_label):
    try:
        # Get values from entries and convert to float
        nums = [
            float(num1_entry.get()),
            float(num2_entry.get()),
            float(num3_entry.get()),
            float(num4_entry.get())
        ]
        lowest = min(nums)
        formatted = int(lowest) if lowest.is_integer() else lowest
        result_label.config(text=f"Lowest Number: {formatted}", fg=SUCCESS)
    except ValueError:
        result_label.config(text="Please enter valid numbers", fg=DANGER)

def init(uname, x, y):
    root = tk.Tk()
    root.title("Find Lowest of Four Numbers")
    root.geometry(f"900x600+{x}+{y}")
    root.configure(bg=DARK)
    root.resizable(False, False)

    back_button = tk.Button(root, text="Back to Home", command=lambda: go_back(uname, x, y, root), font=("Bloxat", 12), fg=DARK, bg=WARNING, relief="flat")
    back_button.place(x=20, y=20)

    title = tk.Label(root, text="Find the Lowest Number", font=("Bloxat", 20), fg=WARNING, bg=DARK)
    title.pack(pady=60)

    entries = []
    for i in range(4):
        label = tk.Label(root, text=f"Number {i+1}:", font=("Bloxat", 14), fg=LIGHT, bg=DARK)
        label.pack(pady=5)

        entry = tk.Entry(root, font=("Bloxat", 14), fg=LIGHT, bg=DARK, bd=0, relief="flat", justify="center", insertbackground=LIGHT)
        entry.pack(pady=5)
        entry.config(highlightthickness=2, highlightbackground=PRIMARY, highlightcolor=PRIMARY)
        entries.append(entry)

    result_label = tk.Label(root, text="", font=("Bloxat", 14), fg=SUCCESS, bg=DARK)
    result_label.pack(pady=20)

    check_button = tk.Button(root, text="Check Lowest", font=("Bloxat", 14), fg=LIGHT, bg=SUCCESS,
                             command=lambda: find_lowest(*entries, result_label), relief="flat")
    check_button.pack(pady=10)

    root.mainloop()
    
if __name__ == "__main__":
    if len(sys.argv) > 3:  
        username = sys.argv[1]
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        init(username, x, y)
    else:
        print("Missing arguments for username or window position.")  # Error handling for missing arguments
