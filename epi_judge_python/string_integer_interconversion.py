from test_framework import generic_test
from test_framework.test_failure import TestFailure

import functools
import string

# Hint: Build the result one digit at a time

def int_to_string(x: int) -> str:
    # the natural algorithm would be to prepend digits to the partial result
    # however, adding a digit to the beginning of a string is EXPENSIVE space, since all remaining digits have to move (b/c string are immutable)
    # this is by going ones digit, tens digit, etc. not so elegant (right to left)

    # A more efficient approach is to add each computed digit to the end (left to right), and then reverse the computed sequence 
    # first get the ones digit, then tens digits, etc. then reverse the num 
    is_negative = False
    if x < 0:
        x = -x 
        is_negative = True

    s = [] 
    while True:
        s.append(chr(ord('0') + x % 10)) # generating a string so add to ascii value of zero 
        # get string value of right most digit
        x //= 10 # get rid of right most digit
        if x == 0: # avoid because integer division by zero
            break

    # adds the negative sign back if is_negative
    return ('-' if is_negative else '') + ''.join(reversed(s))

# CANNOT use library functions like int in Python
# updating a mutable string from the front is slow, see see if its possible to 
# WRITE VALUES FROM THE BACK
def string_to_int(s: str) -> int:
    '''
    def my_function(running_sum, c): 
      return running_sum * 10 + string.digits.index(c)

      running_sum is the curr total
      "51" => 51 
       
       s[0] = 5 
       string.digits.index(CURRENT_DIGIT) => "5" => 5 (int)
      
    '''

    return (-1 if s[0] == '-' else 1) * functools.reduce(lambda running_sum, c: 
                                                            running_sum * 10 + string.digits.index(c), s[s[0] in '-+':], 
                                                            0)
    # reduce(accumulator, current element)
    # 3rd parameter of reduce() => the initializer if the string is empty; default value

def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')

if __name__ == '__main__':
    # print(string_to_int("4176473"))

    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))