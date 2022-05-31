#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in May 2022
# This is the math program, listing numbers in a table and calculating average

import random


def average_numbers(row_list):
    # This function calculates the average of the numbers
    total = 0
    for a_row in row_list:
        for a_single_number in a_row:
            total = total + a_single_number
    return total


def main():
    # This function formats the numbers and does try, catch, input and output
    row_list = []

    # input
    row_string = input("How many rows would you like: ")
    column_string = input("How many columns would you like: ")

    # process & output
    print("")
    try:
        row_integer = int(row_string)
        column_integer = int(column_string)
        for loop_counter_row in range(0, row_integer):
            column_list = []
            for loop_counter_column in range(0, column_integer):
                a_single_number = random.randint(1, 50)
                column_list.append(a_single_number)
                print("{}".format(a_single_number), end=" ")
            row_list.append(column_list)
            print("")
        # call functions
        average = average_numbers(row_list)
        print("\nThe average of all the numbers is {}.".format(average))
    except Exception:
        print("Invalid number!")
        print("\nDone.")


if __name__ == "__main__":
    main()
