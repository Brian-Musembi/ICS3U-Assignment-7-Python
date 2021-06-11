#!/usr/bin/env python3

# Created by Brian Musembi
# Created on June 2021
# This program takes a given number and returns a list of
#       it's digits


def digit_list(user_int):
    # This function finds each digit from a number

    list_of_digits = []
    digit = 0

    # process
    for digit in str(user_int):
        list_of_digits.append(int(digit))

    return list_of_digits


def main():
    # this function receives input and returns output
    print("This program takes a given number and"
          " returns a list of it's digits.")
    print("")

    # input
    while True:
        try:
            user_input = input("Enter any number you want: ")
            user_int = int(user_input)
            print("")

            if user_int:
                # call function
                digits_of_num = digit_list(user_int)

                print("The digits that make up the number {0} are: "
                      .format(user_input))
                print("")

                # printing out each digit from the list
                print("[", end="")

                for digits in digits_of_num:

                    print("{0}".format(digits), end="")

                    # if statement for comma placement
                    if digits != digits_of_num:
                        print(", ", end="")
                    else:
                        pass

                print("]")

                break
            else:
                # output
                print("Please enter a positive integer! Try again.")
                print("")
        except Exception:
            # output
            print("Please enter a number! Try again.")

    print("")
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
