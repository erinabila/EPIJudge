from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:

    def permutations_helper(index, index_set, permutation): 
        if index == len(A):
            res_permutation.append(permutation)
        else: 
            for i in range(len(A)):
                if i not in index_set: 
                    index_set.add(i)
                    permutation.append(A[i])
                    permutations_helper(index + 1, index_set, permutation)


    res_permutation = [] 
    permutations_helper(0, set(), [])
    return res_permutation


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
