"""
169. Majority Element
https://leetcode.com/problems/majority-element/description/

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example:
Input: nums = [3,2,3]
Output: 3
"""


def majorityElement(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    n = len(nums)
    number_log = {}

    for number in nums:
        if number_log.get(number) is not None:
            number_log[number] += 1
            if number_log[number] >= n / 2:
                return number
        else:
            number_log[number] = 1
"""
Intuition:
My immediate thought on how to solve the problem is to keep a dictionary where I would track the number and the amount of instances. If one of those instance became greater or equal to the array length divided by 2, I would return that number.

Approach:
Before learning about the collections and counter functions, the function used a checker to see if the array 'nums' is greater than 1. If not, it'll return the only element. Assuming the array is larger than 1, I would use a dictionary and use a for loop to count every unique number as the key and the amount of instances as their value.
After inserting a second or more instance of any number, the function checks if the dictionary value is greater than n/2, meaning it's the majority. If found, that number will be returned.  

Time complexity: O(n)
The function loops over each number in the input list exactly once. As a result, the time complexity is linear, or O(n), where n is the length of the input list. This linear time complexity is because for each number, the function does a constant amount of work – it either increments the count of that number or initializes it to 1.

Space complexity: O(n)
The function uses a dictionary (number_log) to keep track of the number of occurrences of each number in the input list. In the worst case scenario, all numbers in the list are unique, so the dictionary would have as many entries as there are numbers in the list. As a result, the space complexity is O(n), where n is the length of the input list. This space complexity is linear because the amount of additional space used by the function scales linearly with the size of the input list.
"""
