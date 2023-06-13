Password Manager

This is a simple password manager built using the Tkinter library in Python. It generates secure passwords, stores them locally, and allows you to search for saved passwords associated with a specific website.

Features

Password Generation: The application can generate strong, random passwords that include a mix of uppercase and lowercase letters, numbers, and symbols.
Password Storage: Passwords, along with the associated website and email, are stored locally in a JSON file.
Password Search: You can retrieve the email and password for a specific website that has been stored in the application.

Dependencies

Tkinter: Used to create the graphical user interface.
Pyperclip: Used to copy the generated password to the clipboard.
JSON: Used to store and retrieve the passwords, emails, and websites.

How to Use
Clone this repository:

Copy code
git clone https://github.com/your-username/password-manager.git
Navigate to the cloned repository:

Copy code
cd password-manager
Run the Python script:

Copy code
python3 main.py

Note: Make sure you have Python3 and the required libraries installed on your machine.

Upon launching, the application presents fields for the Website, Email/Username, and Password.

To generate a password, click on the "Generate" button. This will automatically populate the password field with a strong, randomly generated password.

Enter the website and email information, then click on the "Add" button to store the information.

To search for a password, enter the name of the website and click on the "Search" button. If the website's information is stored in the application, a dialog box will appear displaying the email and password. Otherwise, an error message will appear.


Important Note

This is a simple password manager intended for educational purposes. It stores passwords in plaintext in a local file, and therefore should not be used for managing sensitive information.

Contribution

Feel free to contribute to this project by submitting pull requests. Make sure the code is well commented, and the commit messages are meaningful.

License

This project is licensed under the MIT License - see the LICENSE.md file for details.
