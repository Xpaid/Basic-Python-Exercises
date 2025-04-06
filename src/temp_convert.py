import tkinter as tk
import subprocess
import sys
from resources import *

def go_back(uname, x, y, root):
    current_x = root.winfo_x()
    current_y = root.winfo_y()

    root.destroy()
    subprocess.Popen([sys.executable, "src/home.py", uname, str(current_x), str(current_y)])

def convert_temperature(temperature_entry, result_label, conversion_type):
    try:
        # Retrieve the input temperature
        celsius = float(temperature_entry.get())

        # Perform the conversion based on the selected type
        if conversion_type == "Fahrenheit":
            result = (celsius * 9 / 5) + 32
            # Check if the input is an integer, display Celsius as integer if so
            celsius_display = f"{celsius:.1f}" if not celsius.is_integer() else f"{int(celsius)}"
            result_label.config(text=f"{celsius_display}°C = {result:.2f}°F", fg=SUCCESS)
        elif conversion_type == "Kelvin":
            result = celsius + 273.15
            # Display Celsius as integer if it's an integer
            celsius_display = f"{celsius:.1f}" if not celsius.is_integer() else f"{int(celsius)}"
            result_label.config(text=f"{celsius_display}°C = {result:.2f}K", fg=INFO)
    except ValueError:
        result_label.config(text="Please enter a valid number.", fg=DANGER)

def switch_conversion(conversion_button, conversion_type):
    # Switch between conversion types
    if conversion_type.get() == "Fahrenheit":
        conversion_type.set("Kelvin")
        conversion_button.config(text="Convert to Kelvin")
    else:
        conversion_type.set("Fahrenheit")
        conversion_button.config(text="Convert to Fahrenheit")

def init(uname, x, y):
    root = tk.Tk()
    root.geometry("900x600")
    root.title("Temperature Converter")
    root.configure(bg=DARK)
    root.resizable(False, False)
    root.geometry(f"900x600+{x}+{y}") 

    back_button = tk.Button(root, text="Back to Home", command=lambda: go_back(uname, x, y, root),
                            font=("Bloxat", 12), fg=DARK, bg=WARNING, relief="flat")
    back_button.place(x=20, y=20)

    title = tk.Label(root, text="Temperature Converter", font=("Bloxat", 20), fg=WARNING, bg=DARK)
    title.pack(pady=60)

    temperature_label = tk.Label(root, text="Enter Temperature in Celsius:", font=("Bloxat", 14), fg=LIGHT, bg=DARK)
    temperature_label.pack(pady=10)

    temperature_entry = tk.Entry(root, font=("Bloxat", 14), fg=LIGHT, bg=DARK, bd=0, relief="flat", insertbackground=LIGHT, justify="center")
    temperature_entry.pack(pady=10)
    temperature_entry.config(highlightthickness=2, highlightbackground=PRIMARY, highlightcolor=PRIMARY)

    result_label = tk.Label(root, text="", font=("Bloxat", 14), fg=INFO, bg=DARK)
    result_label.pack(pady=10)

    conversion_type = tk.StringVar()
    conversion_type.set("Fahrenheit")

    conversion_button = tk.Button(root, text="Convert to Fahrenheit", font=("Bloxat", 14), fg=LIGHT, bg=SUCCESS,
                                  command=lambda: convert_temperature(temperature_entry, result_label, conversion_type.get()))
    conversion_button.pack(pady=10)

    switch_button = tk.Button(root, text="Switch", font=("Bloxat", 14), fg=LIGHT, bg=INFO,
                              command=lambda: switch_conversion(conversion_button, conversion_type))
    switch_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 3:
        username = sys.argv[1]
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        init(username, x, y)
    else:
        print("Missing arguments for username or window position.")
