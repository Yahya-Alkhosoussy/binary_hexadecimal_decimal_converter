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