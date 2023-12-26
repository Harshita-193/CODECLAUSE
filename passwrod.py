'''  NAME:- HARSHITA GAIKWAD '''

# RANDOM PASSWORD GENERATOR:- 

'''  This password generator generates password for you with random set of integers, alphabets or special characters depending upon you choice.

The options are:- 1] Do you need Uppercase letters in your Password
                  2] Do you need Lowercase letters in you Password
                  3] Do you want Special Characters??
                  4] Do you need Numbers?
                              '''

import random  #for randomness
import string  #to generate a string of password

def generate_password(length=12, uppercase=True, lowercase=True, numbers=True, special_chars=True):
    characters = ""

    if uppercase:         #UPPERCASE GENERATION
        characters += string.ascii_uppercase

    if lowercase:         #LOWERCASE GENERATION
        characters += string.ascii_lowercase

    if numbers:          #NUMBERS GENERATION
        characters += string.digits

    if special_chars:     #GENERATING SPL.CHARACTERS
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type should be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print(" HEYYY!! Welocme to My Random Password Generator!!!")
    
    try:
        length = int(input("Please Enter the desired password length you wish for : "))
        uppercase = input("Do you need uppercase letters? (y/n): ").lower() == 'y'
        lowercase = input("Do you need lowercase letters? (y/n): ").lower() == 'y'
        numbers = input("Do you want to add numbers? (y/n): ").lower() == 'y'
        special_char = input("Do you want to add special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, uppercase, lowercase, numbers, special_char)

        print(f"Your Generated Password is : {password}")

    except ValueError as e:
       print(f"Error: {e}")

if __name__ == "__main__":
    main()
