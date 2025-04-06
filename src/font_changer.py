import tkinter as tk
import subprocess
import sys
from resources import *  

def go_back(uname, x, y, root):
    current_x = root.winfo_x()
    current_y = root.winfo_y()
    
    root.destroy()  
    subprocess.Popen([sys.executable, "src/home.py", uname, str(current_x), str(current_y)]) 

def change_font_style(font_style, label):
    # Change the font of the label based on selected font style
    label.config(font=(font_style, 14))

def init(uname, x, y):
    root = tk.Tk()
    root.geometry("900x600")
    root.title("Font Style Changer")
    root.configure(bg=DARK)
    root.resizable(False, False)
    root.geometry(f"900x600+{x}+{y}")

    back_button = tk.Button(root, text="Back to Home", command=lambda: go_back(uname, x, y, root),
                            font=("Bloxat", 12), fg=DARK, bg=WARNING, relief="flat")
    back_button.place(x=20, y=20)

    title = tk.Label(root, text="Change Font Style", font=("Bloxat", 20), fg=WARNING, bg=DARK)
    title.pack(pady=60)

    # Label to display the text
    label = tk.Label(root, text="This is a sample text", font=("Bloxat", 14), fg=LIGHT, bg=DARK)
    label.pack(pady=50)

    # Buttons to change font style
    font_button_1 = tk.Button(root, text="Change to Arial", font=("Bloxat", 12), fg=LIGHT, bg=PRIMARY,
                              command=lambda: change_font_style("Arial", label), relief="flat")
    font_button_1.pack(pady=10)

    font_button_2 = tk.Button(root, text="Change to Times New Roman", font=("Bloxat", 12), fg=LIGHT, bg=DANGER,
                              command=lambda: change_font_style("Times New Roman", label), relief="flat")
    font_button_2.pack(pady=10)

    font_button_3 = tk.Button(root, text="Change to Courier", font=("Bloxat", 12), fg=LIGHT, bg=SUCCESS,
                              command=lambda: change_font_style("Courier", label), relief="flat")
    font_button_3.pack(pady=10)

    root.mainloop()
    
if __name__ == "__main__":
    if len(sys.argv) > 3:  
        username = sys.argv[1]
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        init(username, x, y)
    else:
        print("Missing arguments for username or window position.")  # Error handling for missing arguments
