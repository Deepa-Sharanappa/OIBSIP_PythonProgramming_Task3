# OIBSIP_PythonProgramming_Task3
A simple Python Tkinter application that generates secure random passwords with customizable options and password strength analysis.

The Random Password Generator is a Python-based desktop application that helps users create strong and secure passwords. The application allows users to customize password length and choose different character types such as letters, numbers, and symbols.
This project is built using Python and Tkinter and includes additional security features such as password strength analysis, exclusion of ambiguous characters, and clipboard integration.

->Objective:
The objective of this project is to develop a user-friendly tool that generates secure and customizable passwords to improve account security and demonstrate concepts such as GUI design, randomization, and input validation.

->Features:
1.Core Features
    Generate random passwords
    User-defined password length
2.Include or exclude:
    Letters
    Numbers
    Symbols
3.Security Features
    Password strength checker (Weak / Medium / Strong)
    Color indicator for password strength
    Minimum password length validation
    Exclusion of confusing characters (O, 0, l, 1, I)
4.Utility Features
    Copy password to clipboard
    Show / Hide generated password
    Generate multiple passwords at once
    Error handling for invalid input


->Technology	Purpose
    Python : Programming language
    Tkinter : GUI development
    Random module	: Random password generation
    String module : Character set

->How the Application Works
    The user enters the desired password length.
    The user selects the character types (letters, numbers, symbols).
    The system creates a character pool based on the selected options.
    The application generates a random password.
    The password strength is analyzed and displayed as:
        Weak  
        Medium
        Strong
    The user can:
        Copy the password to clipboard
        Show or hide the password
        Generate multiple passwords
