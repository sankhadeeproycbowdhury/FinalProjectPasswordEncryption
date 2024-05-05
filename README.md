# YOUR PROJECT TITLE :Secure User Generator
    ## Video Demo: [Secure User Generator](https://youtu.be/4Mv6Sck20jo)
    ## Description:

    ### Secure User Generator

####Overview
The Secure User Generator is a command-line tool designed to facilitate the creation and management of user credentials securely. The program allows users to either manually input their credentials or opt for the system to generate a strong and secure password for them. And then user information is stored in a CSV file securely(in encrypted format) for future reference.Here's a breakdown of the main functionalities:

####Features

*** 1.Command-line Argument Handling: ***
Verifies the correct number of command-line arguments and checks if the provided file is in CSV format.If requirements are not satisfied it terminates program using `sys.exit()`.

*** 2.Date of Birth Validation: ***
Ensures the provided date of birth (DOB) adheres to the DD/MM/YYYY format.
Validates the day, month, and year components for accuracy.Uses `sys.exit()` to terminate program if conditions are not fulfilled.

*** 3.Key Generation: ***
Generates a key based on a combination of the user's password and date of birth.
Matches the key and password length for future references.

*** 4.Encryption and Decryption: ***
Encrypts and decrypts passwords using the generated key.
Handles both numeric and alphanumeric characters during encryption and decryption.
Based on the generated key each character(numeric,alphabetic and special symbols) of password is ciphered,thus encryption is complete.

*** 5.Password Generation: ***
Generates a secure password with a specified length.(specified by the user or uses default length given in the system).
Combines uppercase letters, lowercase letters, symbols, and numbers for password diversity.
Incorporates error handling to catch invalid inputs when specifying the password length.

*** 6.User Interaction: ***
Prompts the user to input a username.
Provides an option to either generate a password or manually input one.
Handles user responses, providing flexibility for user input variations.
Prompts the user for their date of birth in DD/MM/YYYY format, if not provided in correct
format the program terminates using `sys.exit()`.
Finally generates the key and encrypts the password.
Returning a dictionary of `{"username":username , "password":en_psd}`.

*** 7.Main Loop: ***
Allows users to create multiple user entries.
Terminates the loop based on user input, with improved handling for both "yes" and "no" responses.

*** 8.CSV File Handling: ***
Writes user information (username and encrypted password) to a CSV file.
Uses the csv.DictWriter class to organize data in rows.

*** 9.Execution Control: ***
The main function (main()) orchestrates the overall flow of the program.

*** 10.Improved User Interaction: ***
Provides more informative messages based on user input.
Recognizes and handles variations in user responses.


####Usage####

*** Command-line Arguments: ***
Ensure that user provide the correct command-line arguments:

`python project.py user.csv`

*** User Interaction: ***
Follow the prompts to enter a username, choose password generation or manual input, and provide additional information as needed.

*** CSV Output: ***
The program stores user information in the specified CSV file, including usernames and encrypted passwords.

*** Termination: ***
The program can be terminated by entering "no" or similar variations during the user creation loop.


####Explanation

Overall, this project  provides a simple yet effective way to manage user credentials securely, combining password generation with user interaction and CSV file handling.
The command-line interface makes it convenient for users to create and store multiple user accounts.
The project contains five files namely : project.py , test_project.py , user.csv , README.md , requirements.txt .
Each file serves a specific purpose.
Like, requirements.txt has a list of all pip-installable libraries that my project uses.
README.md explains my project.It include my Project title, the URL of my video and a description of my project.
user.csv is a csv file that stores each user credentials created by the program,which include username and encrypted password.
test_project.py contains four fuctions namely : **test_check_arg**,**test_get_dob**,**test_get_key**,**test_encrypt**.
Each of them tests the fuction assigned to them individually.For example test_check_arg tests the check_arg fuction with help of `assert` key word  and `pytest` module.
Finally, project.py contains the entire code of the project.
Imports random , sys , csv and contains funtions namely: **check_arg**,**get_dob**,**get_key**,**encrypt**,**decrypt**,**get_password**,**generate_user** and **mainfuction** . Please go through the features section to know more about these functions individually.

####Contributors

[Sankhadeep RoyChowdhury]
Feel free to contribute to the project by adding new features, improving existing functionalities, or fixing any issues. Bug reports and feature requests are also welcome.


###New Features

#Previously the project used a csv file to store the user-data.But now all the data are stored inside users.db.
There is no more any need of giving an extra command-line argument for the csv-file.Every thing is now automated
and made more userfriendly , well tuned.

