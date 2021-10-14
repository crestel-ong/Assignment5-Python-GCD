#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Oct 2021
# This GCD program


def main():
    # this function finds the greatest common divisor(factor) of 2 #s

    # input
    first_number_as_string = input("Enter the first integer: ")
    second_number_as_string = input("Enter the second integer: ")

    try:
        # convert string to integer
        first_number_as_integer = int(first_number_as_string)
        second_number_as_integer = int(second_number_as_string)

        # process and output
        if first_number_as_integer > second_number_as_integer:
            smaller_number = second_number_as_integer
        else:
            smaller_number = first_number_as_integer

        for counter in range(1, smaller_number + 1):
            if (
                first_number_as_integer % counter == 0
                and second_number_as_integer % counter == 0
            ):
                GCD = counter
        print("")
        print(
            "The GCD (greatest common divisor) of these two numbers is {0}.".format(GCD)
        )
    except Exception:
        print("")
        print("Invalid input.")
    print("\nDone.")


if __name__ == "__main__":
    main()
