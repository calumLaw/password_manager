Password Manager

This is a simple password manager project built with Python's Tkinter library. It generates secure passwords, saves your login credentials for various websites, and allows you to copy generated passwords to your clipboard.

Features

Password Generation: The manager generates secure random passwords based on a mix of letters, numbers, and symbols. Passwords can be copied to your clipboard automatically.
Save Credentials: The manager allows you to save your login credentials (Website, Email/Username, Password) for various websites.
GUI: A clean and straightforward graphical user interface is built using the Tkinter library.

How to Use

Clone this repository to your local machine using git clone https://github.com/your_username/password-manager.git.

Install the required packages:

Tkinter comes pre-installed with the standard Python distribution, so you don't need to install anything.
Install the Pyperclip library using pip install pyperclip.
Run the script using python password_manager.py.

Use the GUI to generate and store passwords.

Code Overview

The code includes the following functions:

generate_password: Generates a secure password, copies it to the clipboard, and inserts it into the password field in the GUI.

save_data: Saves the entered website, email, and password to a text file. If any of these fields are left empty, it will show a prompt.

The UI has been developed using the Tkinter library. It includes input fields for entering the website, email, and password details. It also includes buttons to generate a password and add the entered details to the text file.

Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License

MIT License
