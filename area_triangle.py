#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: November 2019
# This program calculates the area of a triangle


def calculate(base, height):
    # This function calculates the area of a triangle

    # Process
    area = (base*height)/2

    # Output
    print("")
    print("The area of the triangle is {0}cm²".format(area))


def main():
    # This function gets the base and height then calls the calculate function
    print("We will be calculating the area of a triangle.")
    print("")

    # Input
    while True:
        base_from_user = input("Enter the base in cm (integer): ")
        height_from_user = input("Enter the height in cm (integer): ")

        try:
            base_from_user = int(base_from_user)
            height_from_user = int(height_from_user)
            calculate(base_from_user, height_from_user)
            if base_from_user == int(base_from_user) and\
               height_from_user == int(height_from_user):
                break
            else:
                print("Error!")
        except Exception:
            print("Error!")
            print("")


if __name__ == "__main__":
    main()
