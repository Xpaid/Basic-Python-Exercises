import tkinter as tk
import subprocess
import sys
from resources import *

def go_back(uname, x, y, root):
    current_x = root.winfo_x()
    current_y = root.winfo_y()

    root.destroy()
    subprocess.Popen([sys.executable, "src/home.py", uname, str(current_x), str(current_y)])

# Function to add two binary numbers
def add_binary_numbers(binary1_entry, binary2_entry, result_label, decimal_label):
    try:
        # Retrieve binary numbers from the entries
        binary1 = binary1_entry.get()
        binary2 = binary2_entry.get()

        # Validate the inputs to ensure they are binary numbers
        if not all(bit in '01' for bit in binary1) or not all(bit in '01' for bit in binary2):
            result_label.config(text="Please enter valid binary numbers!", fg=DANGER)
            decimal_label.config(text="")  # Clear the decimal label if error
            return

        # Add the binary numbers
        sum_binary = bin(int(binary1, 2) + int(binary2, 2))[2:]
        sum_decimal = int(sum_binary, 2)

        # Display the result in binary and decimal
        result_label.config(text=f"Sum: {sum_binary} (Binary)", fg=SUCCESS)
        decimal_label.config(text=f"Decimal Equivalent: {sum_decimal}", fg=SUCCESS)

    except Exception as e:
        result_label.config(text=f"Error: {e}", fg=DANGER)
        decimal_label.config(text="")  # Clear the decimal label on error

def init(uname, x, y):
    root = tk.Tk()
    root.geometry("900x600")
    root.title("Add Binary Numbers")
    root.configure(bg=DARK)
    root.resizable(False, False)
    root.geometry(f"900x600+{x}+{y}") 

    back_button = tk.Button(root, text="Back to Home", command=lambda: go_back(uname, x, y, root),
                            font=("Bloxat", 12), fg=DARK, bg=WARNING, relief="flat")
    back_button.place(x=20, y=20)  

    title = tk.Label(root, text="Add Binary Numbers", font=("Bloxat", 20), fg=WARNING, bg=DARK)
    title.pack(pady=60)

    binary1_label = tk.Label(root, text="Binary Number:", font=("Bloxat", 14), fg=LIGHT, bg=DARK)
    binary1_label.pack(pady=10)

    binary1_entry = tk.Entry(root, font=("Bloxat", 14), fg=LIGHT, bg=DARK, bd=0, relief="flat", insertbackground=LIGHT, justify="center")
    binary1_entry.pack(pady=10)
    binary1_entry.config(highlightthickness=2, highlightbackground=PRIMARY, highlightcolor=PRIMARY)

    binary2_label = tk.Label(root, text="Second Binary:", font=("Bloxat", 14), fg=LIGHT, bg=DARK)
    binary2_label.pack(pady=10)

    binary2_entry = tk.Entry(root, font=("Bloxat", 14), fg=LIGHT, bg=DARK, bd=0, relief="flat", insertbackground=LIGHT, justify="center")
    binary2_entry.pack(pady=10)
    binary2_entry.config(highlightthickness=2, highlightbackground=PRIMARY, highlightcolor=PRIMARY)

    add_button = tk.Button(root, text="Add Binary", font=("Bloxat", 14), fg=LIGHT, bg=SUCCESS,
                           command=lambda: add_binary_numbers(binary1_entry, binary2_entry, result_label, decimal_label),
                           relief="flat")
    add_button.pack(pady=20)

    # Result label to show the binary sum
    result_label = tk.Label(root, text="Sum: N/A", font=("Bloxat", 16), fg=INFO, bg=DARK)
    result_label.pack(pady=10)

    # Decimal result label to show the decimal equivalent
    decimal_label = tk.Label(root, text="Decimal Equivalent: N/A", font=("Bloxat", 16), fg=INFO, bg=DARK)
    decimal_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 3:
        username = sys.argv[1]
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        init(username, x, y)
    else:
        print("Missing arguments for username or window position.")  # Error handling for missing arguments
