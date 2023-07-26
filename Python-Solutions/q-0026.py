"""
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
def removeDuplicates(nums: list[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

"""
Intuition
If we want to remove duplicates in-place, one way is to use two pointers: one to iterate over the array and another to indicate the position to overwrite with a new distinct element.

Approach
We initialize a pointer 'j' to 1, which points to the second element in the list. We then iterate over the list from the second element using 'i'. If the current element 'nums[i]' is different from the previous element 'nums[i - 1]', it means we've found a new distinct number, so we overwrite the number at position 'j' with 'nums[i]' and increment 'j' by 1.
At the end of the function, 'j' represents the length of the list without duplicates since it's been incremented each time we've found a distinct number.

Time complexity: O(n)
We iterate over the list once, where n is the length of the list. This results in a linear time complexity.

Space complexity: O(1)
We only use a constant amount of space to store 'i' and 'j', regardless of the input size. The space complexity is thus constant, O(1).
"""