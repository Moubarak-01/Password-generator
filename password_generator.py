import random
import string
from tkinter import Tk, Label, Button, Entry

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        password_label.config(text="Please enter a valid number!")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="Generated Password: " + random_password)

# GUI setup
window = Tk()
window.title("Password Generator")

Label(window, text="Password Length:").pack()
length_entry = Entry(window)
length_entry.insert(0, "12")  # Default length
length_entry.pack()

password_label = Label(window, text="Generated Password:")
password_label.pack()

Button(window, text="Generate Password", command=generate_password).pack()

window.mainloop()
