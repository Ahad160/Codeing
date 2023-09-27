import tkinter as tk

# Create a window
window = tk.Tk()

# Bengali text
bengali_text = "Java programming এর প্রয়োগক্ষেত্র উল্লেখ কর।"

# Create a label to display the text
label = tk.Label(window, text=bengali_text, font=("Arial", 12))
label.pack()

# Run the GUI
window.mainloop()
