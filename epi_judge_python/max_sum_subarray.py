from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    # base case 
    if len(A) == 0:
        return 0

    B = [0] * len(A)
    B[0] = A[0]
    res_max = B[0]

    for i in range(1, len(A)):
        # restart subarray OR continue my current contiguous subarray        
        B[i] = max(A[i], B[i-1] + A[i])
        res_max = max(res_max, B[i])    

    return 0 if res_max < 0 else res_max


if __name__ == '__main__':
    A=[-2, 3, 1, -7, 3, 2, -1]
    # print(find_maximum_subarray(A))

    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
