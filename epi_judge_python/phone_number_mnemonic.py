from typing import List
from test_framework import generic_test, test_utils
"""
TIME COMPLEXITY: O(N * 4^N)
    - N rep the number of digits in the phone number 
    - Since there are no more than 4 possible characters FOR EACH DIGIT, the number of recursive calls means its at most O(4^N)
"""
# The mapping from digit to corresponding characters.
MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ') # tuple value type
# digit =   0    1     2      3      4      5      6       7      8       9
# ^ phone number's index = digit variable 
def phone_mnemonic(phone_number: str) -> List[str]:
    def phone_mnemonic_helper(digit: int) -> None:
        # reached the end 
        if digit == len(phone_number):
            # All digits are processed, so add partial_mnemonic to mnemonics.
            # (We add a copy since subsequent calls modify partial_mnemonic.)
            mnemonics.append(''.join(partial_mnemonic)) # partial_mnemonic[] to str as an element appended to mnemonics[] - O(N) 
        else: # otherwise do recursion! 
            # Try all possible characters for this digit.
            for c in MAPPING[int(phone_number[digit])]: # we check every letter from the mapping tuple at phone number's index(int) 
                partial_mnemonic[digit] = c
                phone_mnemonic_helper(digit + 1) # move on to next digit - O(4^N) 

    mnemonics: List[str] = []
    partial_mnemonic = ['0'] * len(phone_number)
    phone_mnemonic_helper(0)
    return mnemonics

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
