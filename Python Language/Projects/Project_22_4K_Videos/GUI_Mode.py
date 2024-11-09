import tkinter as tk
from tkinter import ttk


# Initialize the main application window
root = tk.Tk()
root.title("4K Download")

# Load the Azure theme
try:
    root.tk.call("source", r"E:\Codeing\Python Language\GUI\Azure-ttk-theme-main\Azure-ttk-theme-main\azure.tcl")  # Replace with the correct path to azure.tcl
    root.tk.call("set_theme", "light")  # Use "dark" for dark mode
except tk.TclError:
    print("Azure theme file not found. Please check the path to 'azure.tcl'.")

# Main label
label = ttk.Label(root, text="Hello with Azure Theme!")
label.pack(padx=20, pady=20)

# Set a minsize for the window and center it
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

# Add a label above the entry box
entry_label = ttk.Label(root, text="Enter the link:", anchor="w")
entry_label.pack(padx=20, pady=(10, 0), fill="x")

# Add a ttk entry box with placeholder functionality
placeholder_text = "Enter the Link"

entry = ttk.Entry(root, width=30)
entry.insert(0, placeholder_text)
entry.pack(padx=20, pady=10)

# Function to show placeholder if the entry is empty
def check_placeholder(event=None):
    if entry.get() == "":
        entry.insert(0, placeholder_text)
        entry.config(foreground="gray")
    elif entry.get() == placeholder_text:
        entry.delete(0, tk.END)
        entry.config(foreground="black")

# Set initial color for placeholder
entry.config(foreground="gray")

# Bind events to manage placeholder behavior
entry.bind("<FocusIn>", check_placeholder)
entry.bind("<FocusOut>", check_placeholder)
entry.bind("<KeyRelease>", check_placeholder)  # Check after every key release


# Apply the style to the button
accent_button = ttk.Button(root, text="Download", style='Accent.TButton')
accent_button.pack(padx=20, pady=(10, 20))

# Run the application
root.mainloop()
