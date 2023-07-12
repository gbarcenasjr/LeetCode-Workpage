"""
1. Two Sum
https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""


def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                output = [i, j]
                return output


if __name__ == '__main__':
    example_2 = [3, 2, 4]
    print(twoSum(example_2, 6))

"""
Intuition
The idea is simple: for each number in the list, we need to check if there is another number in the list that, when added to the current number, equals the target.

Approach
The function uses two nested for loops to iterate over the 'nums' list. The outer loop goes through each element in the list, while the inner loop checks every other element in the list starting from the element next to the one currently being evaluated in the outer loop.
If the sum of the current pair of numbers equals the target, the function immediately returns a list containing the indices of the pair. If no such pair is found after checking all possible pairs, the function will naturally return None as no return statement is executed.

Time complexity: O(n^2)
There are two nested loops in the function, and each loops over 'n' elements, where 'n' is the length of the list. Therefore, the time complexity is O(n^2).

Space complexity: O(1)
The function only uses a constant amount of space to store the indices of the pair and does not depend on the size of the input list, thus the space complexity is constant, O(1).
"""
