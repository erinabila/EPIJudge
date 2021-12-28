from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# TIME COMPLEXITY: O(n + m)
# SPACE COMPLEIXTY: O(1) since we resuse the existing nodes 
def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next 

        tail = tail.next 

    # appends the remaining nodes of L1 or L2 
    tail.next = L1 or L2 # cause EITHER OR list exists
    return dummy_head.next # skips/removes dummy head


if __name__ == '__main__':
    # L1 = [2, 5, 7]
    # L2 = [3, 11]

    # print(merge_two_sorted_lists(L1, L2))

    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
