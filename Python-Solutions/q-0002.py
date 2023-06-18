"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example: (These are LinkedLists, not arrays or lists)
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l3 = ListNode(-1)
    current_node = ListNode(-1)
    carry_over = 0

    while l1 is not None and l2 is not None:
        sum = (l1.val + l2.val + carry_over) % 10
        carry_over = (l1.val + l2.val + carry_over) // 10

        new_node = ListNode(sum)

        if l3.val != -1:
            current_node.next = new_node
            current_node = current_node.next
        else:
            l3 = new_node
            current_node = l3

        l1 = l1.next
        l2 = l2.next

    while l1 is not None:
        sum = (l1.val + carry_over) % 10
        carry_over = (l1.val + carry_over) // 10

        new_node = ListNode(sum)

        current_node.next = new_node
        current_node = current_node.next

        l1 = l1.next

    while l2 is not None:
        sum = (l2.val + carry_over) % 10
        carry_over = (l2.val + carry_over) // 10

        new_node = ListNode(sum)

        current_node.next = new_node
        current_node = current_node.next

        l2 = l2.next

    if carry_over != 0:
        new_node = ListNode(carry_over)
        current_node.next = new_node
        current_node = current_node.next

    return l3

"""
Intuition
My thoughts when answering the question was to add the first elements of each pair of LinkedList (LL for short). Then I would contunue until the values were greater than 10, causing an error. Since each element in the LL needs to be 1 digit long, I would need to use modulus to stript the number to the 1's place and any digit after would be carryed over to the next element calculation.

Approach
I initialized 3 variables, both 'l3' (representing the head of the new LL) and 'current_node' as ListNodes with value of -1 since all input will be non-negative, making it distict that these values are not to be inserted. The 'carry_over' will retain the 1 you carry over if the current sum is greater than 9.
The first while loop is used while both the 'l1' and 'l2' LL still contain elements not iterated yet. Both elements of the same place will be added and the 'sum' will equal the modulus of the sum of both Node values and any carry_over value. The 'carry_over' will equal to the floor division of the calculation of 10
(For example: if the sum would have been equal "13", the 'sum' variable will get the 3 of "13" while the 'carry_over' will get the 1 of "13" and use it to be added in the next element place.)
Then, 'new_node' will be created with the 'sum' variable as the Node value. If the new LL 'l3' does not have a valid node (l3.val == -1), then 'l3' will be replaced with the 'new_node' as the head of the node and the 'current node' will be pointing at 'l3'. If there is a valid value in 'l3' (l3.val != -1), then the 'new_node' will be pointed by the 'current_node' next value. Then the 'current_node' will then become the next node pointed. Both 'l1' and 'l2' will be iterated to it's next node continuing the iteration.
The next two while loops are very similiar to the previous one with the difference being if either 'l1' or 'l2 has a larger LL than the other, then the 'sum' values will be inserted to the next nodes in 'l3' through the 'current_node' variable.
Finally, there are edge cases or rare instances where after all the nodes in both LL are calculated, there is still a carry over value to be inserted. Therefore, a 'new_node' is inserted using the 'carry_over' as its node value and inserted into 'l3'.
Afterwards, we call the head of the new LL 'l3' to be returned. Since this is the head node of the LL, it will contain all the nodes of the calculated sum in backward order as the question specifies.


Time complexity: O(n)
Since the function iterates as many times as the largest LL inserted, occassionally one more time if any carry_over value is found at the end, then at worst, the time complexity of this operation would be O(n + 1), or can be simplified to O(n), where n is the length of the largest LL inserted.

Space complexity: O(n)
Since the function creates a LL as large as the largest LL inserted, occassionally plus one if any carry_over value is found at the end, then at worst, the space complexity of this operation would be O(n + 1), or can be simplified to O(n), where n is the length of the largest LL inserted.
"""