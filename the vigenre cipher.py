# Delera, Aritz B.
# The Vigenere Code Cipher

# import pyfiglet module
import pyfiglet

opening = pyfiglet.figlet_format("= O.O.P =", font="starwars")
print(opening)

# Define a class for Vigenere Cipher
class VigenereCipher:
    def __init__(self):
        # create a dictionary to change the alphabets to numbers
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.alphabet_to_numbers = {letter: i for i, letter in enumerate(self.alphabet)}
    
    def encrypt(self, message, key):
        # convert the key to numerical values
        number_of_key = [self.alphabet_to_numbers[letter] for letter in key]

        # encrypt the message using the Vigenère cipher
        cipher_txt = ''
        index_of_key = 0
        for character in message:
            # Add the character to the ciphertext without encrypting it if it is not an alphabet.
            if character not in self.alphabet:
                cipher_txt += character
            else:
                # Determine each letter's numerical value in the message.
                 number = self.alphabet_to_numbers[character]
                # Calculate the result modulo 26 by adding the total number of the alphabet in the key.
                 encrypted_number = (number + number_of_key[index_of_key]) % 26
                # Add the alphabet to the ciphertext after converting the encrypted numerical value to a alphabet.
                 encrypted_alphabet = self.alphabet[encrypted_number]
                 cipher_txt += encrypted_alphabet
                # Move to the next alphabet in the key.
                 index_of_key = (index_of_key + 1) % len(number_of_key)
        return cipher_txt

# Create an introduction
print("=" * 61)
print("\033[32m Welcome to AritzMetic's Vigenère Cipher! \033[0m".center(70, "+"))
print("=" * 61)

# Use while loop for a condition-controlled loop
while True:
    # Ask the name of the user to create a greeting
    name = input("\033[34mHi Smart Pipol! what is your name?\033[0m")
    print("\033[40mHi", name, "! AritzMetic is here to help you in Ciphering your code!\033[0m")
    # ask the user to input the message and key
    message = input("\033[31mWhat is the message of your secret code?: \033[0m")
    key = input("\033[32mHow about the key of your secret code?: \033[0m")
    # Create an instance of VigenereCipher class and encrypt the message using the key
    cipher = VigenereCipher()
    ciphertext = cipher.encrypt(message.upper(), key.upper())
    # Display the encrypted message
    print("\033[40mYown! The process has been completed! The Ciphertext of your secret message and key is", ciphertext, ".\033[0m")
    # Ask the user if they want to continue or exit
    question = input("\033[34mWould you like to continue?? (yes or no): \033[0m")
    if question.lower() == "no":
        closing = pyfiglet.figlet_format("Thank you for using AritzMetic's Vigenere Cipherer. Have a nice day!", font="puffy")
        print(closing)
        break