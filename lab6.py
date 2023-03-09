"""
Author: Ryan Smith
Description: Program that encodes and decodes a password
Date: 3/9/23
"""


def encode(password):
    encoded = ''
    for digit in password:
        dig = int(digit)
        if dig < 7:
            encoded += str(dig + 3)
        else:
            encoded += str(dig - 7)
    return encoded


def main():
    menu = 'Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n'
    while True:
        print(menu)
        choice = int(input('Please enter an option: '))
        if choice == 1:
            password = encode(input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!')
        elif choice == 2:
            pass
        elif choice == 3:
            break
        print()


if __name__ == "__main__":
    main()
