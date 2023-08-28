"""
27. Remove Element
https://leetcode.com/problems/remove-element/description/

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the
elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following
things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The
  remaining elements of nums are not important as well as the size of nums.
- Return k.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


def removeElement(nums: list[int], val: int) -> int:
    counter = 0
    i = 0
    while i < len(nums):
        if nums[i] == val:
            for j in range(i, len(nums) - 1):
                nums[j] = nums[j + 1]
            nums.pop()
        else:
            counter += 1
            i += 1
    return counter

"""
Intuition
The goal is to remove all instances of a given value (`val`) from the list `nums` in place and then return the 
new length of the modified `nums`. As we remove an instance of `val`, we shift the remaining elements in the 
list to the left.

Approach
1. Use a variable `counter` to keep track of the number of elements that aren't equal to `val`.
2. Iterate through the `nums` list using an index `i`.
3. If the current element is equal to `val`, we shift all elements to the right of this element to the left by 
   one position and then remove the last element of the `nums` list.
4. If the current element isn't equal to `val`, we increment the `counter` and the index `i`.
5. The final value of `counter` gives the new length of the modified `nums`.

Time Complexity: O(n^2)
For each instance of `val` in the `nums` list, we may need to shift up to `n` elements, resulting in a 
quadratic time complexity.

Space Complexity: O(1)
The space used by the algorithm itself (excluding the input) is constant because we only use a few variables 
and modify the input list in place.
"""