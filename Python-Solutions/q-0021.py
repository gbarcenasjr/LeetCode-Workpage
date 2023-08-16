"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/description/

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(head: ListNode):
    output = "["
    while head:
        output += str(head.val)
        if head.next:
            output += ", "
        head = head.next
    output += "]"
    print(output)


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    prehead = ListNode(-1)  # Creates a placeholder node to set up for the real head of the merged list
    prev = prehead

    while list1 and list2:
        if list1.val <= list2.val:
            prev.next = list1
            list1 = list1.next
        else:
            prev.next = list2
            list2 = list2.next
        prev = prev.next

    if list1:
        prev.next = list1
    else:
        prev.next = list2

    return prehead.next


if __name__ == '__main__':
    list1_example1 = ListNode(1, ListNode(2, ListNode(4)))
    list2_example1 = ListNode(1, ListNode(3, ListNode(4)))
    mergedList = mergeTwoLists(list1_example1, list2_example1)
    printList(mergedList)

"""
Intuition
The objective is to merge two sorted linked lists into one sorted list. We can compare the nodes' values from both
lists one-by-one and append the node with the smaller value to the merged list.

Approach
1. Initialize a `prehead` node with an arbitrary value (-1). This node is a placeholder for subsequent operations.
2. Use another node pointer, `prev`, to track the current node in the merged list.
3. Loop while there are nodes left in both `list1` and `list2`:
   - Compare the current nodes in `list1` and `list2`.
   - If `list1`'s value is smaller or equal, link `prev` node's next pointer to this node from `list1` and move
     forward in `list1`.
   - If `list2`'s value is smaller, link `prev` node's next pointer to this node from `list2` and move forward in
     `list2`.
   - Update `prev` to its next node.
4. Post-loop, if nodes remain in `list1` or `list2`, link them to the `prev` node (they are sorted).
5. The merged list starts after `prehead`.

Time Complexity: O(m + n)
Where `m` and `n` are the lengths of `list1` and `list2` respectively. We may need to traverse both lists entirely.

Space Complexity: O(1)
No extra space proportional to input size is used. The merged list uses the nodes of the given lists.
"""