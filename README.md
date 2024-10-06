# binary_hexadecimal_decimal_converter


## Backend functions:

### 1. decimal_to_binary(number)

Here is the possible explanation behind some of the code that may or may not be confusing in the function:

- `Remainder_list` it is a list of the remainders when dividing by two which is either a 1 or a 0 through the modulus function, and the 0 or 1 is the binary code, you might observe that this is not the answer normally, but I will talk about that later.

- `While number >= 2` why 2? because it will be confusing if I went to 1

- `remainder = number % 2` the modulus function is the function that divides the variable number by 2 and finds out if it has a remainder, if it does then it will return 1, if it doesn't then it will return 0

- `for i in range(len(remainder_list) -1, -1, -1)`: there are a lot to unpack here so, new list:

1. `len(remainder_list) -1` why subtract 1? well if 1 is not subtracted from it, it will start from an index that does not exist, normal *for* loops that may look like `for i in range(len(remainder_list))` which is basically the same as `for i in range(0, len(remainder_list), 1)` where 0 is the starting point, len(remainder_list) is the end point where it stops when it reaches that point and the variable i is incremented by 1. Using this logic, we can infer that using the maximum first is not a good idea as it stops 1 before that, so we need to subtract one from the maximum point to have similar results.

2. the first `-1` this is similar to the last point, this is the end point

3. the second `-1` this is also similar to the 1 in the first point, this is how i is incrememnted aka -1 is added to i every time it loops.

### 2. binary_to_decimal(number)

- `string` this variable is basically just transforming the number we get into a string so it can be later separated into individual digits

- `num_list` this array is where all invdividual digits of binary go to be multiplied by their respective power of 2

### 3. hexadecimal_to_decimal(number)

**note: these were made hours apart so if they do not follow the same methods that is the reason, but they all work so does it really matter?**

- `hex` this is the dictionary that contains all the hexadecimal values and their decimal equivalent.

- `hex_str` this is the string equivalent for the hexadecimal value given to the function to be split in the for loop

### 4. Decimal_to_hexadecimal(number)

- `hexadecimal_list` this is similar to the dictionary to the last function, but it uses an array this time, my main reasoning was to see if I can do it, no other reason.

- `for i in range(len(hexadecimal_number) -1, -1, -1)` This for loop is similar to the one used in the decimal to binary function, and this is crucial for this as when I was testing the functions it returned the inverse of what was the value, for example A0 was shown as 0A, and 0A = A ≠ A0 due to the nature of these number systems, this is like saying 10 = 01 = 1 because it is the reverse, which is obviously not true.

**5 and 6 do not need explanations**
