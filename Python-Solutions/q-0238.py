"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


def productExceptSelf(nums: list[int]) -> list[int]:
    answer_array = []

    for i in range(len(nums)):
        if i == 0:
            answer_array.append(1)
            continue
        answer_array.append(answer_array[i - 1] * nums[i - 1])

    prev = 1
    for i in range(len(nums) - 1, -1, -1):
        if i != len(nums) - 1:
            prev *= nums[i + 1]
            answer_array[i] *= prev

    return answer_array


if __name__ == '__main__':
    example1 = [1, 2, 3, 4]
    print(productExceptSelf(example1))

"""
Intuition
The aim is to compute the product of all elements in the list except for the current one without using 
division. The idea is to first get the product of all elements to the left of the current element and then 
multiply it with the product of all elements to the right of the current element.

Approach
1. Start with an initial product of 1 (since no numbers to the left of the first element).
2. For each element in the `nums` list, store the product of all elements to its left in the `answer_array`.
3. After getting the left products, iterate through the `nums` list in reverse to get the product of all 
   elements to the right of the current element.
4. As we move through the list in reverse, we keep track of the product of all elements to the right of 
   the current element using the `prev` variable.
5. Multiply the left product (from the `answer_array`) with the right product (using the `prev` variable) 
   to get the final product for each element.

Time Complexity: O(n)
We iterate through the `nums` list twice (once forwards and once backwards), resulting in a linear time 
complexity.

Space Complexity: O(1)
Despite the `answer_array` used to store results, the space used by the algorithm itself (excluding 
the input and output) is constant because we only use a few variables.
"""
