import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A: List[int]) -> None:
    '''
    - Required to solve it without allocating additional storage
    - Should take advantage of the fact that you can operate efficiently on both ends
    - GOAL: reorder its entries so that the even entires appear first
    '''
    leftPtr, rightPtr = 0, len(A) - 1

    while leftPtr < rightPtr:
        # if even
        if A[leftPtr] % 2 == 0:
            leftPtr += 1
        # else odd
        else:
            # swap w/o using temp variable 
            A[leftPtr], A[rightPtr] = A[rightPtr], A[leftPtr]
            # from if statement we know that after swapping, the A[rightPtr] is now ODD thus we
            # don't care about A[rightPtr] anymore and shift rightPtr to check next element from this end
            rightPtr -= 1
    return A

@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
