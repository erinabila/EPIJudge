from typing import List

from test_framework import generic_test


def max_rectangle_submatrix(A: List[List[bool]]) -> int:
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_submatrix.py', 'max_submatrix.tsv',
                                       max_rectangle_submatrix))
