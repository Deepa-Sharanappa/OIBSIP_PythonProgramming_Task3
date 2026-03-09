import random
import string
import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Password Strength Checker
# -------------------------------
def check_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Medium"
    else:
        return "Strong"


# -------------------------------
# Generate Single Password
# -------------------------------
def generate_password():

    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")
        return

    if length < 6:
        messagebox.showerror("Error", "Password length must be at least 6")
        return

    characters = ""

    if letters_var.get():
        characters += string.ascii_letters

    if numbers_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showerror("Error", "Select at least one character type")
        return

    # Exclude confusing characters
    exclude = "O0l1I"
    characters = ''.join(c for c in characters if c not in exclude)

    password = ""

    for i in range(length):
        password += random.choice(characters)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    # Check password strength
    strength = check_strength(password)

    if strength == "Weak":
        strength_label.config(text="Password Strength: Weak", fg="red")
    elif strength == "Medium":
        strength_label.config(text="Password Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Password Strength: Strong", fg="green")


# -------------------------------
# Generate Multiple Passwords
# -------------------------------
def generate_multiple():

    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")
        return

    characters = string.ascii_letters + string.digits + string.punctuation

    passwords = ""

    for i in range(5):
        password = ''.join(random.choice(characters) for i in range(length))
        passwords += password + "\n"

    messagebox.showinfo("Generated Passwords", passwords)


# -------------------------------
# Copy Password
# -------------------------------
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")


# -------------------------------
# Show / Hide Password
# -------------------------------
def toggle_password():

    if password_entry.cget('show') == "":
        password_entry.config(show="*")
    else:
        password_entry.config(show="")


# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()
root.title("Password Generator")
root.geometry("380x350")

title = tk.Label(root, text="Random Password Generator", font=("Arial", 14, "bold"))
title.pack(pady=10)

tk.Label(root, text="Password Length").pack()

length_entry = tk.Entry(root)
length_entry.pack()

letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)

password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

strength_label = tk.Label(root, text="Password Strength: ")
strength_label.pack(pady=5)

tk.Button(root, text="Show / Hide Password", command=toggle_password).pack(pady=5)

tk.Button(root, text="Copy Password", command=copy_password).pack(pady=5)

tk.Button(root, text="Generate 5 Passwords", command=generate_multiple).pack(pady=5)

root.mainloop()