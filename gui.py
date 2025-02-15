import tkinter as tk
from tkinter import ttk

# Function to be called when any button is pressed
def on_button_press(button_number):
    check_status = check_var.get()
    status_text = "checked" if check_status else "unchecked"
    response_label.config(text=f"Button {button_number} Pressed! Checkbox is {status_text}.")

# Function to read the selected options from the listbox
def read_selected_options():
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(i) for i in selected_indices]
    response_label.config(text=f"Selected options: {', '.join(selected_items)}")

# Create the main window
root = tk.Tk()
root.title("Modern Tkinter App with Multi-Select Dropdown")

# Set window size
window_width = 500
window_height = 400

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position for the window to be centered
position_x = (screen_width // 2) - (window_width // 2)
position_y = (screen_height // 2) - (window_height // 2)

# Set the geometry of the window
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

# Set a modern style
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TLabel', font=('Helvetica', 12), padding=10)
style.configure('TCheckbutton', font=('Helvetica', 12), padding=10)

# Create a frame to hold the buttons in a row
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

# Create and pack five buttons
for i in range(1, 6):
    button = ttk.Button(button_frame, text=f"Button {i}", command=lambda i=i: on_button_press(i))
    button.pack(side=tk.LEFT, padx=5)

# Create a listbox for multi-select options
listbox_frame = ttk.Frame(root)
listbox_frame.pack(pady=10)

listbox_label = ttk.Label(listbox_frame, text="Select Options:")
listbox_label.pack()

listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE, height=6)
options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
for option in options:
    listbox.insert(tk.END, option)
listbox.pack()

# Create a button to read selected options
read_button = ttk.Button(listbox_frame, text="Read Selected Options", command=read_selected_options)
read_button.pack(pady=5)

# Create a checkbox
check_var = tk.BooleanVar()
checkbutton = ttk.Checkbutton(root, text="Check me", variable=check_var)
checkbutton.pack(pady=10)

# Create the response label
response_label = ttk.Label(root, text="")
response_label.pack(pady=10)

# Run the main loop
root.mainloop()
