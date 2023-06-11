from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# Generate password
def generate_password():
    pw_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    pw_input.insert(0, password)


# Save password to file

def save_data():
    email = email_input.get()
    website = website_input.get()
    password = pw_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty.")
    else:
        ok_to_save = messagebox.askokcancel(title=website_input.get(),
                                            message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it ok to save? ")

        if ok_to_save:
            with open("passwords.txt", "a") as file:
                file.write(f"\n{website} | {email} | {password}")
            website_input.delete(0, END)
            pw_input.delete(0, END)


#  UI

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "example@email.com")
pw_input = Entry(width=26)
pw_input.grid(column=1, row=3)

# Buttons
generate_btn = Button(text="Generate", command=generate_password)
generate_btn.grid(column=2, row=3, columnspan=2, sticky="w")
add_btn = Button(text="Add", width=35, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
