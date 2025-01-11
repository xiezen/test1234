# Save this as simple_gui.py
import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Hello", "Hello, World!")

def main():
    root = tk.Tk()
    root.title("Simple GUI")
    
    button = tk.Button(root, text="Click Me", command=on_button_click)
    button.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()
