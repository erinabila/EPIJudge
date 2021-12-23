from test_framework import generic_test

# TIME COMPLEXITY - O(N)
# SPACE COMPLEXITY - O(1)
def is_palindromic(s: str) -> bool:
    # Rather than creating a new string for the reverse of the input string O(n),
    # make it traverse the input string forwards and backwards to save space O(1)
    
    # Note that s[~i]for i in [0, len(s) - 1] is s[-(i + 1)]
    # On a integer value is ~i = -(i + 1) = -i - 1

    # EPI SOLUTION
    # return all(s[i] == s[~i] for i in range(len(s) // 2))

    # MY UNDERSTANDING FROM THE EPI SOLUTION
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
        print("s[", i, "]   ", s[i], "s[-", i, "- 1] ", s[~i])
    return True

if __name__ == '__main__':
    print(is_palindromic("abcba"))
    print(is_palindromic("abcdfcba"))

    # exit(
    #     generic_test.generic_test_main('is_string_palindromic.py',
    #                                    'is_string_palindromic.tsv',
    #                                    is_palindromic))
