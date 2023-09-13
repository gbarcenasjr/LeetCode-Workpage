""""
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
 the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in
 non-decreasing order. The final sorted array should not be returned by the function, but instead be stored inside the
 array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that
 should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
        Do not return anything, modify nums1 in-place instead.
    """
    for x in range(n):
        nums1.insert(m, nums2[x])
        nums1.pop(-1)
    nums1.sort()


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print("BEFORE:")
    print(f"nums1 = {nums1}, m = {m}, nums2 = {nums2}, n = {n}")

    merge(nums1,m,nums2,n)

    print("AFTER:")
    print(f"nums1 = {nums1}")

"""
Intuition
The objective is to merge two sorted arrays (nums1 and nums2). Since nums1 has enough space to hold the combined
elements, the goal is to merge the elements in-place, ensuring the sorted order.

Approach

Loop through each element of nums2:
Insert each element of nums2 to the end of the portion of nums1 that contains valid elements (position m).
Remove the last element from nums1 to maintain its original size.
After merging, sort nums1.
Time Complexity: O(n log n)
The sorting step at the end has a complexity of O(n log n), where n is the length of nums1.

Space Complexity: O(1)
The solution merges the arrays in-place without using additional space that scales with the input size.
"""