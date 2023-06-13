from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            pw_input.delete(0, END)


# Search passwords

def show_dialog(title, text):
    top = Toplevel()
    top.title(title)

    text_widget = Text(top, height=10, width=40)
    text_widget.insert(END, text)
    text_widget.pack()

    text_widget.configure(state="disabled")  # make it read-only


def find_password():
    website = website_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="No Data File Found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            show_dialog("Email/Username and Password",
                        f"Email/Username: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops!", message=f"No details for {website} exists")


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
website_input = Entry(width=30)
website_input.grid(column=1, row=1)
website_input.focus()
email_input = Entry(width=30)
email_input.grid(column=1, row=2)
email_input.insert(0, "example@email.com")
pw_input = Entry(width=30)
pw_input.grid(column=1, row=3)

# Buttons
search_btn = Button(text="Search", command=find_password)
search_btn.grid(column=2, row=1, )
generate_btn = Button(text="Generate", command=generate_password)
generate_btn.grid(column=2, row=3, columnspan=2)
add_btn = Button(text="Add", width=35, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
