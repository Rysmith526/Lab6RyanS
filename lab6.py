"""
Author: Ryan Smith
Description: Program that encodes and decodes a password
Date: 3/9/23
"""


def encode(password):  # Encodes an inputted password
    encoded = ''
    for digit in password:
        dig = int(digit)
        if dig < 7:
            encoded += str(dig + 3)
        else:
            encoded += str(dig - 7)
    return encoded


def decode(message):
    decoded = ''
    for digit in message:
        new_digit = str((int(digit) - 3) % 10)
        decoded += new_digit
    return decoded


def main():
    password = 0
    menu = 'Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n'
    while True:
        print(menu)
        choice = int(input('Please enter an option: '))
        if choice == 1:
            # Calls encode function to store encoded password
            password = encode(input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!')
        elif choice == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}.')
        elif choice == 3:
            break
        print()


if __name__ == "__main__":
    main()
