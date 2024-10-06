mode = 0


def decimal_to_binary(number):

    remainder_list = []

    while number >= 2:

        remainder = number % 2

        remainder_list.append(remainder)

        number = number // 2
    
    if number == 1:

        remainder_list.append(1)
    
    if number == 0: 

        remainder_list.append(0)
    
    binary_number = ""

    for i in range(len(remainder_list) -1, -1, -1):

        binary_number += str(remainder_list[i])

    return binary_number

def binary_to_decimal(number):

    num_list = []

    string = str(number)

    for digit in string:

        if digit != " ":

            num_list.append(int(digit))

    decimal_number = 0

    for num in range(len(num_list)):

        decimal_number += num_list[num] * (2 ** num)

    return decimal_number

def hexadecimal_to_decimal(number):

    hex = {
       "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, 
       "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
    }

    decimal_number = 0

    hex_str = str(number).upper()

    for digit in hex_str:

        decimal_number = decimal_number * 16 + hex[digit]


    return decimal_number

