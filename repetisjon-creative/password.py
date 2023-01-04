# create a prompt where the user is asked to create an account with a username
# and a password
# the password should be between 8 and 16 in length
# and must contain a number, a lowercase letter and an uppercase letter

import re

def createUsername():
    username = input('Username: ')
    return username

def createPassword():
    password = input('Password: ')
    repeat = input('Repeat password: ')
    if checkPassword(password, repeat):
        return password
    
    return createPassword()

def checkPassword(password, repeat):
    if checkLength(password) and checkRepeat(password, repeat) and checkCharacters(password):
        return True
    return False

def checkRepeat(password, repeat):
    if password == repeat:
        return True
    print('Passwords do not match. Try again.')
    return False

def checkLength(password):
    if len(password) >= 8 and (len(password) <= 16):
        return True
    print('Length of password must be between 8 and 16 characters. Try again.')
    return False

def checkCharacters(password):
    if lowerCheck(password) and upperCheck(password) and numberCheck(password):
        return True
    return False

def lowerCheck(password):
    lower = 'qwertyuiopåasdfghjkløæzxcvbnm'
    for letter in password:
        if letter in lower:
            return True
    print('Password must contain a lowercase letter. Try again.')
    return False

def upperCheck(password):
    upper = 'qwertyuiopåasdfghjkløæzxcvbnm'.upper()
    for letter in password:
        if letter in upper:
            return True
    print('Password must contain a uppercase letter. Try again.')
    return False

def numberCheck(password):
    numbers = '1234567890'
    for letter in password:
        if letter in numbers:
            return True
    print('Password must contain a number. Try again.')
    return False

# we must now require an email instead of a username for the login, but 
# keep the option of the username 
# the email must have a '@', and end in '.no', '.com' or '.org'
def registerEmail():
    email = input('Email: ')
    if isValidEmail(email):
        return email
    return registerEmail()

def isValidEmail(email):
    return re.match(r'^[\w\.\+-]+@[\w\.-]+\.[a-zA-Z]{2,}$', email)

def main():
    print('You will now create a user!')
    username = createUsername()
    email = registerEmail()
    password = createPassword()
    print(username)
    print(password)

main()

# the user should be asked to put their first and last-name, and the program 
# should then use their first-name in all subsequent prompts


# put the code into nice functions


# we must store the password hashed - use the hashlib-module!


# next up we are going to store the information in a binary-file


