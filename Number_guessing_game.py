#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: Mar 2022
# This program is a number guessing game

import constants


def main():
    # This function checks the number

    # input
    number = int(input("Enter number between 0 - 9: "))

    # process & output
    print("")
    if number == constants.right_number:
        print("You guessed right!")
    if number != constants.right_number:
        print("You guessed wrong!")

    print("\nDone.")


if __name__ == "__main__":
    main()
