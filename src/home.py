import tkinter as tk
import subprocess
import sys
from resources import *  

def run_script(script_name, uname, x, y, home_root):
    try:
        # Store the current position of the window before destroying it
        current_x = home_root.winfo_x()
        current_y = home_root.winfo_y()

        home_root.destroy()  # Destroy the current home window
        subprocess.Popen([sys.executable, script_name, uname, str(current_x), str(current_y)])  # Open the new script
    except Exception as e:
        print(f"Error running {script_name}: {e}")

def back_to_login(root):
    current_x = root.winfo_x()
    current_y = root.winfo_y()
    root.destroy()
    subprocess.Popen([sys.executable, "src/login.py", str(current_x), str(current_y)]) 

def exit_program(root):
    root.quit()

def init_home(uname, x, y):
    root = tk.Tk()
    root.geometry("900x600")
    root.title("Home Page")
    root.configure(bg=DARK)
    root.resizable(False, False)
    root.geometry(f"900x600+{x}+{y}")  

    main_frame = tk.Frame(root, bg=DARK)
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    title_label = tk.Label(main_frame, text=f"Welcome {uname}", font=("Bloxat", 30, "bold"), fg=SUCCESS, bg=DARK, height=2)
    title_label.pack(pady=5)

    left_frame = tk.Frame(main_frame, bg=DARK)
    left_frame.pack(side="left", fill="both", expand=True, padx=(20, 20), pady=0)
    inner_left = tk.Frame(left_frame, bg=DARK)
    inner_left.pack(expand=True, fill="both", pady=0)

    inner_left.grid_rowconfigure(0, weight=1)
    inner_left.grid_columnconfigure(0, weight=1)

    content_frame = tk.Frame(inner_left, bg=DARK)
    content_frame.grid(row=0, column=0, sticky="n")

    menu_label = tk.Label(content_frame, text="Menu", font=("Bloxat", 20, "bold"), fg=WARNING, bg=DARK, height=2)
    menu_label.pack(pady=5)

    button_frame = tk.Frame(content_frame, bg=DARK)
    button_frame.pack(fill="both", expand=True)  # Ensuring button_frame expands vertically

    buttons = [
        ("1. Grading System", "src/grading_system.py"),
        ("2. Octal to Decimal", "src/oct_dec.py"),
        ("3. Add Binary Numbers", "src/binary_Add.py"),
        ("4. Temp Converter", "src/temp_convert.py"),
        ("5. Font Style Changer", "src/font_changer.py"),
        ("6. Bitwise Calculator", "src/bitwise_calc.py"),
        ("7. Find Lowest Number", "src/lowest.py"),
        ("8. Letters Only Textbox", "src/letters_only.py"),
        ("9. Reverse Name", "src/reverse_name.py"),
        ("10. Personal Info Display", "src/my_profile.py"),
        ("Back to Login", "back_to_login"),
        ("Exit", "exit_program")  
    ]

    for (text, script) in buttons:
        if script == "back_to_login":
            btn = tk.Button(button_frame, text=text, width=30, font=("Bloxat", 12),
                            fg=DARK, bg=WARNING, height=1, bd=0,
                            activebackground=PRIMARY, activeforeground="white",
                            relief="flat", cursor="hand2", 
                            command=lambda root=root: back_to_login(root))  
        elif script == "exit_program":
            btn = tk.Button(button_frame, text=text, width=30, font=("Bloxat", 12),
                            fg=DARK, bg=WARNING, height=1, bd=0,
                            activebackground=PRIMARY, activeforeground="white",
                            relief="flat", cursor="hand2", 
                            command=lambda root=root: exit_program(root))  # Exit functionality
        else:
            btn = tk.Button(button_frame, text=text, width=30, font=("Bloxat", 12),
                            fg=DARK, bg=WARNING, height=1, bd=0,
                            activebackground=PRIMARY, activeforeground="white",
                            relief="flat", cursor="hand2", 
                            command=lambda script=script: run_script(script, uname, x, y, root))  # Pass the correct script dynamically
        btn.pack(pady=5)

        def on_enter(e, b=btn): b.config(bg=PRIMARY, fg="white")
        def on_leave(e, b=btn): b.config(bg=WARNING, fg=DARK)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    # Right side (your picture area)
    right_frame = tk.Frame(main_frame, width=300, height=400, bg=DARK, relief="flat", bd=0)
    right_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
    right_frame.pack(side="right", fill="both", expand=False, padx=(0, 75), pady=40)

    # Load the image after the root window is created
    img = load_image('me1.jpg')  # Assuming load_image() returns an image object
    image_label = tk.Label(right_frame, image=img, bg=DARK, bd=0, padx=0, pady=0)
    image_label.pack(expand=True, padx=0, pady=0)
    # Retain a reference to the image to prevent garbage collection
    image_label.image = img

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 3:
        username = sys.argv[1]
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        init_home(username, x, y)
    else:
        print("Missing arguments for username or window position.")
