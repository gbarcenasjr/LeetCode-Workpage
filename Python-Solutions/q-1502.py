"""
1502. Can Make Arithmetic Progression From Sequence
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

Example:
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
"""


def canMakeArithmeticProgression(arr: list[int]) -> bool:
    arr.sort()
    difference = abs(arr[0] - arr[1])

    for index in range(1, len(arr) - 1):
        if abs(arr[index] - arr[index + 1]) != difference:
            return False
    return True


if __name__ == '__main__':
    array = [3, 5, 1]
    output = canMakeArithmeticProgression(array)
    print(output)

"""
Intuition
When I saw this problem at first, I knew that absolute values will be needed to calculate the differences between numbers in an array. I would also needed to sort the array or the differences between numbers will be inaccurate.

Approach
Using Python's built-in sort method, I was able to sort the array numerically. Then I grabbed the first two elements of the array to calculate the difference. This difference will be our "Pass" condition for any other element in the array. The for loop will test if the difference between the current element and the next element is equal to the difference we found in the first two elements. If all elements have the same difference between numbers, the function will return True.

Time complexity: O(n log(n))
Python's sort method has a worst case time complexity of O(n log(n)).
The for loop in the iterate through every element of the array once. This would result in a time complexity of O(n).
So when combining the time complexity O(n log(n)) and O(n), the overall time complexity will be O(n log(n)).

Space complexity: O(1)
Since the only additional value stored in this function would be the int variable "difference." Therefore, this function has a constant space complexity or O(1).
"""
