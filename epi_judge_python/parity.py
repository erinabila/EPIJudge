from test_framework import generic_test

# TIME COMPLEXITY: O(n)
# def parity(x: int) -> int:
#     ''' 
#     set output to 1 IF the # of ones in the word(input) is odd
#         input: 1011       output: 1
#         input: 10001000   output: 0
#     '''
#     result = 0
#     while x:
#         result ^= x & 1 # result = result ^ (x & 1)
#         # ^ rep XOR (True if and only if one side is True, not both)
#         # & rep Bitwise Multiplication, both sides need to be True, TO MASK ALL THE ONES
#         x >>= 1  # shift to right to remove left most side digit
#     return result

# TIME COMPLEXITY: O(k) where k is the # of bits set to 1 in a particular word (so # of 1s)
def parity(x: int) -> int:
    result = 0
    while x: 
        result ^= 1
        x &= x - 1 # drops the lowest set bit of x, so base10 20 minus 1 equal base10 19 but its written in bits here (base2)
    return result 



if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
