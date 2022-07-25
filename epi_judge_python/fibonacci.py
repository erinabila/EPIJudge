from test_framework import generic_test


def fibonacci(n: int) -> int:

    pass

'''
    # ITERATIVE APPROACH 
    num1, num2 = 0, 1 
    if n == 0:
        return num1
    elif n == 1: 
        return num2

    temp_num = 0
    for _ in range(2, n + 1):
        # 0, 1, 1, 2, 3, 5, ..... 
        # fib(0) = 0, fib(1) = 1, fib(2) = 1
        temp_num = num1 + num2 
        num1 = num2 
        num2 = temp_num 
    
    return temp_num 
'''



'''
    # RECURSIVE APPROACH - VERY SLOW!!!
    if n < 2: 
        return n

    return fibonacci(n - 1) + fibonacci(n - 2) 
'''


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
