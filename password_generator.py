import random
import string
from tkinter import Tk, Label, Button

window = Tk()
window.title("Password Generator")



def generate_password():
    random_password = ""

    random_password += random.choice(string.ascii_letters)
    random_password += random.choice(string.ascii_letters)
    random_password += random.choice(string.ascii_letters)
    random_password += random.choice(string.ascii_letters)

    random_password += str(random.randint(0, 9))
    random_password += str(random.randint(0, 9))
    random_password += str(random.randint(0, 9))
    random_password += str(random.randint(0, 9))

    # Update the label with the generated password
    password_label.config(text="Generated Password: " + random_password)


# Create a label to display the generated password
password_label = Label(window, text="Generated Password: ")

# Create a button to trigger password generation
generate_button = Button(window, text="Generate Password", command=generate_password)

# Pack the label and button
password_label.pack()
generate_button.pack()

window.mainloop()