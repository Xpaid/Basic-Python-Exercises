import tkinter as tk
import subprocess
import sys
from resources import *  

def go_back(uname, x, y, root):
    current_x = root.winfo_x()
    current_y = root.winfo_y()
    
    root.destroy()  
    subprocess.Popen([sys.executable, "src/home.py", uname, str(current_x), str(current_y)]) 

def bitwise_operations(num1, num2, shift_value, result_label):
    try:
        # Convert inputs to integers
        num1 = int(num1)
        num2 = int(num2)
        shift_value = int(shift_value)

        # Perform the bitwise operations
        and_result = num1 & num2
        or_result = num1 | num2
        xor_result = num1 ^ num2
        not_result = ~num1
        left_shift_result = num1 << shift_value
        right_shift_result = num1 >> shift_value

        # Combine binary and decimal results into one string
        result_text = (
            f"AND: {bin(and_result)} ({and_result})\n"
            f"OR: {bin(or_result)} ({or_result})\n"
            f"XOR: {bin(xor_result)} ({xor_result})\n"
            f"NOT: {bin(not_result)} ({not_result})\n"
            f"Left Shift: {bin(left_shift_result)} ({left_shift_result})\n"
            f"Right Shift: {bin(right_shift_result)} ({right_shift_result})"
        )

        # Update the result_label to show combined binary and decimal results
        result_label.config(text=result_text, fg=SUCCESS)

    except ValueError:
        result_label.config(text="Please enter valid integers", fg=DANGER)

def init(uname, x, y):
    root = tk.Tk()
    root.geometry("900x600")
    root.title("Bitwise Calculator")
    root.configure(bg=DARK)
    root.resizable(False, False)
    root.geometry(f"900x600+{x}+{y}") 

    back_button = tk.Button(root, text="Back to Home", command=lambda: go_back(uname, x, y, root),
                            font=("Bloxat", 12), fg=DARK, bg=WARNING, relief="flat")
    back_button.place(x=20, y=20)  

    title = tk.Label(root, text="Bitwise Calculator", font=("Bloxat", 20), fg=WARNING, bg=DARK)
    title.pack(pady=60)

    # First number input
    num1_label = tk.Label(root, text="Enter First Integer:", font=("Bloxat", 14), fg=LIGHT, bg=DARK)
    num1_label.pack(pady=10)

    num1_entry = tk.Entry(root, font=("Bloxat", 14), fg=LIGHT, bg=DARK, bd=0, relief="flat", insertbackground=LIGHT, justify="center")
    num1_entry.pack(pady=10)
    num1_entry.config(highlightthickness=2, highlightbackground=PRIMARY, highlightcolor=PRIMARY)

    # Second number input
    num2_label = tk.Label(root, text="Enter Second Integer:", font=("Bloxat", 14), fg=LIGHT, bg=DARK)
    num2_label.pack(pady=10)

    num2_entry = tk.Entry(root, font=("Bloxat", 14), fg=LIGHT, bg=DARK, bd=0, relief="flat", insertbackground=LIGHT, justify="center")
    num2_entry.pack(pady=10)
    num2_entry.config(highlightthickness=2, highlightbackground=PRIMARY, highlightcolor=PRIMARY)

    # Shift value input
    shift_value_label = tk.Label(root, text="Enter Shift Value (for << and >>):", font=("Bloxat", 14), fg=LIGHT, bg=DARK)
    shift_value_label.pack(pady=10)

    shift_value_entry = tk.Entry(root, font=("Bloxat", 14), fg=LIGHT, bg=DARK, bd=0, relief="flat", insertbackground=LIGHT, justify="center")
    shift_value_entry.pack(pady=10)
    shift_value_entry.config(highlightthickness=2, highlightbackground=PRIMARY, highlightcolor=PRIMARY)

    # Calculate button
    calculate_button = tk.Button(root, text="Calculate", font=("Bloxat", 14), fg=LIGHT, bg=SUCCESS,
                                 command=lambda: bitwise_operations(num1_entry.get(), num2_entry.get(), shift_value_entry.get(), result_label),
                                 relief="flat")
    calculate_button.pack(pady=20)

    # Result label to show the operation results (combined binary and decimal)
    result_label = tk.Label(root, text="", font=("Bloxat", 14), fg=INFO, bg=DARK)
    result_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 3:  
        username = sys.argv[1]
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        init(username, x, y)
    else:
        print("Missing arguments for username or window position.")  # Error handling for missing arguments
