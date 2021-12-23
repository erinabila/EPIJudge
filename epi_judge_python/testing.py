import copy
from typing import List


print('Euclid,Axiom 5, Parallel Lines'.split(','))

print(3 * '01')

print(','.join(('Gauss', 'Prince of Mathmeticians', '1777-1855')))



# def longest_equal_subarray(A: List[int])-> int:
#     # TODO: Write a program that takes an array of integers and finds the length of a longest subarray all of whose entries are equal
#     window_start, window_end = 0, 0
#     length = 0
#     for i in range(len(A) - 1):
#         if A[i] == A[i + 1]:
#             window_end += 1
#         else:
#             length = max(length, window_end - window_start + 1)
#             window_start = i
#             window_end = i
#         print("Window start", window_start,  "   window end", window_end, " A[i]",   A[i])
#     return length
# A = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8]
# print(longest_equal_subarray(A))