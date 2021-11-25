from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    '''
    TODO Takes input of an array of digits encoding a nonnegative decimal integer D and updates the array to represent the integer D + 1
    ex) input = <1, 2, 9> then you should update the array to <1, 3, 0>
    '''
    '''
    MY SOLUTION
        TIME COMPLEXITY: O(n)
        SPACE COMPLEXITY: O(n) (?)
    '''
    carry_out = 0
    for i in reversed(range(len(A))):
        # add 1 in the one's digit
        if i == len(A) - 1:
            A[i] += 1
        # check if have carry_out
        if carry_out: # exists 
            A[i] += carry_out
            carry_out = 0
        # check if creates carry_out for next digit
        if A[i] == 10:
            carry_out = 1
            A[i] = 0
    # if need to extend list b/c has carry out at the left most digit
    if A[0] == 0:
         A.insert(0, 1)        
    return A

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
