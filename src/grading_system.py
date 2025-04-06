import tkinter as tk
import subprocess
import sys
from resources import *  

def calculate_final_grade(prelim, midterm, semi_finals, finals):
    try:
        prelim = float(prelim)
        midterm = float(midterm)
        semi_finals = float(semi_finals)
        finals = float(finals)
        
        # Weighted calculation based on the percentages
        final_grade = (prelim * 0.30) + (midterm * 0.20) + (semi_finals * 0.30) + (finals * 0.20)
        return round(final_grade, 2)  # Round to 2 decimal places
    except ValueError:
        return "Invalid input. Please enter valid numbers."

def go_back(uname, x, y, root):
    current_x = root.winfo_x()
    current_y = root.winfo_y()
    
    root.destroy()  
    subprocess.Popen([sys.executable, "src/home.py", uname, str(current_x), str(current_y)]) 

def init(uname, x, y):
    root = tk.Tk()

    root.geometry("900x600")
    root.title("Grading System")  
    root.configure(bg=DARK)  
    root.resizable(False, False) 
    root.geometry(f"900x600+{x}+{y}") 

    back_button = tk.Button(root, text="Back to Home", command=lambda: go_back(uname, x, y, root),
                            font=("Bloxat", 12), fg=DARK, bg=WARNING, relief="flat")
    back_button.place(x=20, y=20)  

    title = tk.Label(root, text="Grading System", font=("Bloxat", 20), fg=WARNING, bg=DARK)
    title.pack(pady=60)

    # Input fields for each term grade
    prelim_label = tk.Label(root, text="Prelim Grade:", font=(Bloxat, 12), fg=PRIMARY, bg=DARK)
    prelim_label.pack(pady=5)
    prelim_entry = tk.Entry(root, font=(Bloxat, 12), fg=LIGHT, bg=DARK, bd=0, insertbackground=PRIMARY, justify= "center")
    prelim_entry.pack(pady=5)
    prelim_entry.config(highlightthickness=1, highlightbackground=PRIMARY, highlightcolor=PRIMARY)
    
    # Midterm input
    midterm_label = tk.Label(root, text="Midterm Grade:", font=(Bloxat, 12), fg=PRIMARY, bg=DARK)
    midterm_label.pack(pady=5)
    midterm_entry = tk.Entry(root, font=(Bloxat, 12), fg=LIGHT, bg=DARK, bd=0, insertbackground=PRIMARY, justify= "center")
    midterm_entry.pack(pady=5)
    midterm_entry.config(highlightthickness=1, highlightbackground=PRIMARY, highlightcolor=PRIMARY)

    # Semi-finals input
    semi_finals_label = tk.Label(root, text="Semi-Finals Grade:", font=(Bloxat, 12), fg=PRIMARY, bg=DARK)
    semi_finals_label.pack(pady=5)
    semi_finals_entry = tk.Entry(root, font=(Bloxat, 12), fg=LIGHT, bg=DARK, bd=0, insertbackground=PRIMARY, justify= "center")
    semi_finals_entry.pack(pady=5)
    semi_finals_entry.config(highlightthickness=1, highlightbackground=PRIMARY, highlightcolor=PRIMARY)

    # Finals input
    finals_label = tk.Label(root, text="Finals Grade:", font=(Bloxat, 12), fg=PRIMARY, bg=DARK)
    finals_label.pack(pady=5)
    finals_entry = tk.Entry(root, font=(Bloxat, 12), fg=LIGHT, bg=DARK, bd=0, insertbackground=PRIMARY, justify= "center")
    finals_entry.pack(pady=5)
    finals_entry.config(highlightthickness=1, highlightbackground=PRIMARY, highlightcolor=PRIMARY)

    # Function to display the final grade
    def show_final_grade():
        try:
            # Get the grades as float
            prelim = float(prelim_entry.get())
            midterm = float(midterm_entry.get())
            semi_finals = float(semi_finals_entry.get())
            finals = float(finals_entry.get())
            
            # Validate that all fields do not exceed 100
            if any(grade > 100 or grade < 0 for grade in [prelim, midterm, semi_finals, finals]):
                final_grade_label.config(text="Grades should be between 0 and 100.", fg=DANGER)
                return
            
            # Calculate final grade based on weight distribution
            final_grade = (prelim * 0.30) + (midterm * 0.20) + (semi_finals * 0.30) + (finals * 0.20)
            
            # Ensure the final grade does not exceed 100%
            final_grade = min(final_grade, 100)
            
            # Display the final grade and change color based on grade
            if isinstance(final_grade, float):
                if final_grade < 60:
                    final_grade_label.config(text=f"Final Grade: {final_grade}%", fg=DANGER)
                    remarks_label.config(text="Remarks: TF are you doing?", fg=DANGER)
                elif final_grade < 75:
                    final_grade_label.config(text=f"Final Grade: {final_grade}%", fg=WARNING)
                    remarks_label.config(text="Remarks: Fair", fg=WARNING)
                elif final_grade < 90:
                    final_grade_label.config(text=f"Final Grade: {final_grade}%", fg=INFO)
                    remarks_label.config(text="Remarks: Good", fg=INFO)
                else:
                    final_grade_label.config(text=f"Final Grade: {final_grade}%", fg=SUCCESS)
                    remarks_label.config(text="Remarks: Excellent", fg=SUCCESS)
            else:
                final_grade_label.config(text=final_grade, fg=DANGER)
                remarks_label.config(text="Remarks: Invalid Input", fg=DANGER)
        
        except ValueError:
            final_grade_label.config(text="Invalid input. Please enter numeric values.", fg=DANGER)

    # Calculate Button
    calculate_button = tk.Button(root, text="Calculate Final Grade", font=("Bloxat", 14), fg=LIGHT, bg=SUCCESS,
                                command=show_final_grade, relief="flat", width=25)
    calculate_button.pack(pady=20)

    # Label to display the final grade result
    final_grade_label = tk.Label(root, text="Final Grade: N/A", font=("Bloxat", 16), fg=INFO, bg=DARK)
    final_grade_label.pack(pady=20)

    # Label to display remarks based on the final grade
    remarks_label = tk.Label(root, text="Remarks: N/A", font=("Bloxat", 12), fg=INFO, bg=DARK)
    remarks_label.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 3:  
        username = sys.argv[1]
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        init(username, x, y)
    else:
        print("Missing arguments for username or window position.")  # Error handling for missing arguments
