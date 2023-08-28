"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/description/

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""


def searchInsert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    middle = 0

    while left <= right:
        middle = left + (right - left) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    if nums[middle] < target:
        return middle + 1
    else:
        return middle


if __name__ == '__main__':
    example2_nums = [1, 3, 5, 6]
    example2_target = 2

    print(f"Example 2 Demo:\n"
          f"nums = {example2_nums}\n"
          f"target = {example2_target}\n"
          f"Output: {searchInsert(example2_nums, example2_target)}\n")

"""
Intuition
The problem is asking for the index at which the `target` would be if it was inserted in `nums` (which is sorted). This
can be viewed as a modified binary search. Instead of stopping when the target isn't found, the position to insert it is
returned.

Approach
1. Initialize pointers `left`, `right`, and `middle`. `left` starts at the beginning of the list, `right` at the end.
2. Execute a binary search:
   - Calculate `middle` as the average of `left` and `right`.
   - If the middle element is equal to the target, return `middle`.
   - If the middle element is less than the target, set `left` to `middle + 1` to check the right half.
   - Otherwise, set `right` to `middle - 1` to check the left half.
3. After the while loop, if the target isn't found, check if it should be inserted to the right of `middle` or right at
   the `middle` position.

Time Complexity: O(log n)
The algorithm uses binary search which has a logarithmic time complexity.

Space Complexity: O(1)
No additional space is utilized that scales with the input.
"""
