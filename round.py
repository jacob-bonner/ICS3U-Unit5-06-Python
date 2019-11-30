#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: November 2019
# This program rounds numbers given by the user


def rounding(number, decimal_point):
    # This function rounds the user's number

    # Process
    rounded_number = (number[0]*(10**decimal_point))
    rounded_number = rounded_number + 0.5
    rounded_number = int(rounded_number)
    rounded_number = rounded_number/(10**decimal_point)

    return rounded_number


def main():
    # This function takes the user's number then outputs the number rounded

    # List
    rounding_number = []

    # Process
    while True:
        user_number = input("Enter the number you wish to be rounded: ")
        decimal_place = input("Enter how many decimal places you want left: ")

        try:
            user_number = float(user_number)
            decimal_place = int(decimal_place)
            rounding_number.append(user_number)
            if user_number == float(user_number) and \
               decimal_place == int(decimal_place):
                user_rounded_number = rounding(rounding_number, decimal_place)
                print("")
                print("Your number rounded is", user_rounded_number)
                break
            else:
                print("Error, unable to process inputs")
        except Exception:
            print("Error, unable to process inputs")
            print("")


if __name__ == "__main__":
    main()
