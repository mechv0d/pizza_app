import tkinter as tk
from tkinter import messagebox


def error_dialog(title, message):
    """Displays a simple error dialog box."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showerror(title, message)
