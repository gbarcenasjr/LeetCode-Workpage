"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


def containsDuplicate(nums: list[int]) -> bool:
    nums.sort()
    for index in range(len(nums) - 1):
        if nums[index] == nums[index + 1]:
            return True
    return False


if __name__ == '__main__':
    listOfNumbers = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    output = containsDuplicate(listOfNumbers)
    print(output)

"""
Intuition
My first thought towards the problem was a the naive linear search where I would create an array of visited numbers and check if the current number in a for loop matches any number of the array. Sadly, it was too slow of an algorithm.

However, I assumed if the numbers were sorted, then if there are any matches, then they would be next to each other!

Approach
After the sort() method, I used a for loop to check each number in the array "nums", minus the last element, to see if the next element matches. If any two element matches, then the function would return True. However, if none of the elements matches with each other, then the fucntion would return False.

Complexity
Time complexity: O(n logn)
Python's built-in sort method has a time complexity of O(n logn). The for loop iterates linearly through the elements in the array which would be equivalent to O(n). So the time complexity would be O(n + n logn) or can be simplified to O(n logn)

Space complexity: O(1)
Since the function has a only requires a consistent amount of memory for comparison and does not copy any data, the space complexity of the function would be O(1)
"""
