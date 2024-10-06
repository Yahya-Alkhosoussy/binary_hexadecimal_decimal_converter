# binary_hexadecimal_decimal_converter

## GUI:



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

