import tkinter as tk
import subprocess
import sys
from resources import *  # Import the new load_image function

# Function to handle going back to the previous screen
def go_back(uname, x, y, root):
    current_x = root.winfo_x()
    current_y = root.winfo_y()

    root.destroy()  
    subprocess.Popen([sys.executable, "src/home.py", uname, str(current_x), str(current_y)])

# Function to initialize the window
def init(uname, x, y):
    root = tk.Tk()
    root.geometry("900x600")
    root.title("Personal Information")
    root.configure(bg=DARK)
    root.resizable(True, True)  # Allow resizing of the window
    root.geometry(f"900x600+{x}+{y}")

    # Back button at the top-left corner
    back_button = tk.Button(root, text="Back to Home", command=lambda: go_back(uname, x, y, root),
                            font=("Bloxat", 12), fg=DARK, bg=WARNING, relief="flat")
    back_button.place(x=20, y=20)

    # Title Label with proper color and font
    title = tk.Label(root, text="Personal Information", font=("Bloxat", 20, "bold"), fg=WARNING, bg=DARK)
    title.pack(pady=60)

    # Equal margin spacing
    margin_left = 100  # Adjusted for centering
    margin_top = 150
    vertical_spacing = 40  # Vertical space between elements
    window_width = 900  # Assuming the window width is 900px for positioning the image

    # Left Frame for personal information (positioned manually)
    name_label = tk.Label(root, text="Full Name: Jetro P. Apilado", font=("Bloxat", 14), fg=DARK, bg=LIGHT)
    name_label.place(x=margin_left, y=margin_top)

    # Birthday Label
    birthday_label = tk.Label(root, text="Birthday: 2004 July 07", font=("Bloxat", 14), fg=DARK, bg=LIGHT)
    birthday_label.place(x=margin_left, y=margin_top + vertical_spacing)

    #location
    location_label = tk.Label(root, text="Location: Philippines", font=("Bloxat", 14), fg=DARK, bg=LIGHT)
    location_label.place(x=margin_left, y=margin_top + 2 * vertical_spacing)

    # Likes Description
    likes_label = tk.Label(root, text="Likes: Coding and playing games", font=("Bloxat", 14), fg=DARK, bg=LIGHT)
    likes_label.place(x=margin_left, y=margin_top + 3 * vertical_spacing)
    
    #field
    cs_label = tk.Label(root, text="Field of Study: Computer Science", font=("Bloxat", 14), fg=DARK, bg=LIGHT)
    cs_label.place(x=margin_left, y=margin_top + 4 * vertical_spacing)

    # Right Frame for the Image (positioned manually)
    image_x_position = window_width - 400  # Position the image 300px from the right edge for symmetry

    try:
        image = load_image('me2.jpg')  # Replace with your actual image file
        picture_label = tk.Label(root, image=image, bg=DARK)
        picture_label.image = image  # Keep a reference to the image to prevent garbage collection
        picture_label.place(x=image_x_position, y=margin_top)  # Image positioned on the right side
    except Exception as e:
        picture_label = tk.Label(root, text="Image not found", font=("Bloxat", 14), fg=DANGER, bg=DARK)
        picture_label.place(x=image_x_position, y=margin_top)  # Error message in the same location

    root.mainloop()

# Entry point for the program
if __name__ == "__main__":
    if len(sys.argv) > 3:  
        username = sys.argv[1]
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        init(username, x, y)
    else:
        print("Missing arguments for username or window position.")
