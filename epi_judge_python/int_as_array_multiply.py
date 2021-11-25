from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    '''
    TODO Take two arrays representing integers, and return an integer representing their PRODUCT
    Example 1:
    123 * 987 = 12401 
        7 * 123 * [1]   = 861
        8 * 123 * [10]  = 9840
        9 * 123 * [100] = 110700
        n1  n2          + --------
                          121401           
    '''
    # TEXTBOOK SOLUTION
    # they're m partial products, each with at most n + 1 digits
    # We perform O(1) operations on each digit in each partial product, so the time complexity is O(nm)

    # check if numbers are negative
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1 # ^ is XOR b/c two negatives/positives makes a positive (False), 
    # else if EITHER num is negative then its product is negative (True) so change sign to sign = -1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    # initialize result[] to be length sum of num1[] and num2[], filled with all zeroes inside
    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))): # from index on ones digit to left most digit
        for j in reversed(range(len(num2))): # from index on ones digit to left most digit
            result[i + j + 1] += num1[i] * num2[j] # get current product of the corresponding i and j index digit
            result[i + j] += result[i + j + 1] // 10 # get the ten's digit of current product to that element
            result[i + j + 1] %= 10 # put the one's digit of current product to the next element thus the +1
    
    '''
    When you use enumerate(), the function gives you back two loop variables:
        1) The COUNT of the current iteration
        2) The VALUE of the item at the current iteration
    Example:
        for count, value in enumerate(values):
            print(count, value)
    You don't need to remember to access the item from the iterable, and you don't need to remember to advance the index
    at the end of the loop. Its done automatically in Python!

    Why "i for i"?
    - List comprehensions do not have a built in iterator, and need a loop construct to work
    - i.e.) "i in range(51)" is a boolean expression, not a loop and thus it should be "i for i in range(51)"

    next()
    - Return the next item in an iterator
    '''
    # Remove the leading zeroes
    result = result[next((i for i, x in enumerate(result)
                        if x != 0), len(result)):] or [0]
    # from left to right digits in result[], if its not zero then move to next element until reach zero and shrinks to new size for result[]
    # else it is a zero then set result is zero

    # check if need to change to negative then concatenate from index 1 to end of of result[]
    return [sign * result[0]] + result[1:] 

    # MY SOLUTION: GOT UP TO SUM, BUT UNABLE TO CONVERT INTEGER SUM TO INTEGER LIST B/C OF NEGATIVE SIGN IN FRONT
    # carry_out = 1
    # sum = 0

    # # get num2 as one number, not a list 
    # strings = [str(i) for i in num2] # convert each integer in num2[] to a string
    # two_string = "".join(strings) # "" and iterable as the list of string to concatenate them
    # two_integer = int(two_string) # two_string as obj to convert it to an integer

    # # multiple num2 with each num1 digit and corresponding carry_out
    # for i in reversed(range(len(num1))):
    #     sum += carry_out * two_integer * num1[i]
    #     carry_out *= 10    
    
    # # convert int to List[int], cannot convert to string then convert to list b/c of the negative sign would be its
    # # own element in the list which is not valid for a List[int]
    # is_negative = False
    # res = []

    # # check is sum if negative
    # if sum < 0:
    #     # convert to positive but create flag that its negative to convert back later
    #     sum *= -1 
    #     is_negative = True

    # sum_string = str(sum) # convert integer to string, to get length later

    # # add sum digits to res[]
    # for i in range(len(sum_string)):
    #     res.append(sum_string.index[i])

    # # convert back to negative, if needed
    # if is_negative:
    #     res[0] *= -1

    # print(res)
    # return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
