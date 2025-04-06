import tkinter as tk
import subprocess
import sys
from resources import *  

def go_back(uname, x, y, root):
    current_x = root.winfo_x()
    current_y = root.winfo_y()
    
    root.destroy()  
    subprocess.Popen([sys.executable, "src/home.py", uname, str(current_x), str(current_y)]) 

def init(uname, x, y):
    root = tk.Tk()

    root.geometry("900x600")
    root.title("Octal to Decimal")  
    root.configure(bg=DARK)  
    root.resizable(False, False) 
    root.geometry(f"900x600+{x}+{y}") 

    back_button = tk.Button(root, text="Back to Home", command=lambda: go_back(uname, x, y, root),
                            font=("Bloxat", 12), fg=DARK, bg=WARNING, relief="flat")
    back_button.place(x=20, y=20)  

    title = tk.Label(root, text="Octale to Decimal", font=("Bloxat", 20), fg=WARNING, bg=DARK)
    title.pack(pady=60)

    def convert_octal_to_decimal():
        # Retrieve the octal input from the entry field
        octal_num = octal_entry.get()

        # Validate the input
        if octal_num == "" or not all(char in "01234567" for char in octal_num):
            result_label.config(text="Please enter a valid octal number!", fg=DANGER)
            return
        
        # Convert octal to decimal
        decimal_num = int(octal_num, 8)

        # Display the result in the label
        result_label.config(text=f"Decimal: {decimal_num}", fg=SUCCESS)

    # Label for Octal input
    octal_label = tk.Label(root, text="Enter an Octal Number:", font=("Bloxat", 14), fg=LIGHT, bg=DARK)
    octal_label.pack(pady=20)

    # Textbox for user to input octal number with dark background and underlined effect
    octal_entry = tk.Entry(root, font=("Bloxat", 14), fg=LIGHT, bg=DARK, bd=0, relief="flat", insertbackground=LIGHT, justify="center")
    octal_entry.pack(pady=10)
    octal_entry.config(highlightthickness=2, highlightbackground=PRIMARY, highlightcolor=PRIMARY)

    # Button to trigger conversion
    convert_button = tk.Button(root, text="Convert to Decimal", font=("Bloxat", 14), fg=LIGHT, bg=SUCCESS, relief="flat",
                            command=convert_octal_to_decimal)
    convert_button.pack(pady=20)

    # Label to display the result
    result_label = tk.Label(root, text="Decimal: N/A", font=("Bloxat", 16), fg=INFO, bg=DARK)
    result_label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 3:  
        username = sys.argv[1]
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        init(username, x, y)
    else:
        print("Missing arguments for username or window position.")  # Error handling for missing arguments
