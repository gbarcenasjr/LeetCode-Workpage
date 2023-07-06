"""
704. Binary Search
https://leetcode.com/problems/binary-search/description/

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""


def search(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = (start + end) // 2

        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            start = middle + 1
        if nums[middle] > target:
            end = middle - 1
    return -1

if __name__ == '__main__':
    example_array = [-1,0,3,5,9,12]
    example_target = 9

    print(search(example_array, example_target))

"""
Intuition
Binary search is a powerful method for searching sorted lists. It works by dividing the list in half and determining which half the target value could be in, effectively reducing the problem size by half with each iteration.

Approach
First, we initialize two pointers: 'start' at the beginning of the list, and 'end' at the end of the list. In each iteration of the while loop, we calculate 'middle', the index halfway between 'start' and 'end'. If the element at 'middle' is the target, we return 'middle'. If the target is greater than the element at 'middle', we update 'start' to 'middle + 1', effectively discarding the left half of the list. If the target is less than the element at 'middle', we update 'end' to 'middle - 1', discarding the right half of the list. If the while loop finishes without finding the target, we return -1 to indicate that the target is not in the list.

Time complexity: O(log n)
In binary search, we halve the problem size with each iteration of the loop. This results in a logarithmic time complexity.

Space complexity: O(1)
The binary search operates directly on the input list and uses only a constant amount of additional space to store pointers and a temporary variable, so the space complexity is constant.
"""