import tkinter as tk
import subprocess
import sys
from resources import *  

def go_back(uname, x, y, root):
    current_x = root.winfo_x()
    current_y = root.winfo_y()
    
    root.destroy()  
    subprocess.Popen([sys.executable, "src/home.py", uname, str(current_x), str(current_y)]) 

# Only allow letters in Text widget
def only_letters_key(event):
    if not event.char.isalpha() and event.char not in ("\b", "\r", "\n"):
        return "break"

def init(uname, x, y):
    root = tk.Tk()
    root.geometry("900x600")
    root.title("The Letters Only Box")
    root.configure(bg=DARK)
    root.resizable(False, False)
    root.geometry(f"900x600+{x}+{y}")

    back_button = tk.Button(root, text="Back to Home", command=lambda: go_back(uname, x, y, root),
                            font=("Bloxat", 12), fg=DARK, bg=WARNING, relief="flat")
    back_button.place(x=20, y=20)

    title = tk.Label(root, text="The Letters Only Box", font=("Bloxat", 20), fg=WARNING, bg=DARK)
    title.pack(pady=60)

    label = tk.Label(root, text="Type something below", font=("Bloxat", 14), fg=LIGHT, bg=DARK)
    label.pack(pady=10)

    # Text widget instead of Entry for larger size
    text_box = tk.Text(root, font=("Bloxat", 14), fg=LIGHT, bg=DARK, 
                       height=10, width=50, bd=0, relief="flat", 
                       insertbackground=LIGHT)
    text_box.pack(pady=10)
    text_box.config(highlightthickness=2, highlightbackground=PRIMARY, highlightcolor=PRIMARY)
    text_box.bind("<Key>", only_letters_key)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 3:  
        username = sys.argv[1]
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        init(username, x, y)
    else:
        print("Missing arguments for username or window position.")  # Error handling for missing arguments
