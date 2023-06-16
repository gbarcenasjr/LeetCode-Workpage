"""
Sort an Array
https://leetcode.com/problems/sort-an-array/description/

Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
"""


def sortArray(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    left_array = nums[:len(nums) // 2]
    right_array = nums[len(nums) // 2:]

    # Recursion
    sortArray(left_array)
    sortArray(right_array)

    # Merge
    i = 0  # left_array index
    j = 0  # right_array index
    k = 0  # merged array index
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            nums[k] = left_array[i]
            i += 1
        else:
            nums[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        nums[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        nums[k] = right_array[j]
        j += 1
        k += 1

    return nums


if __name__ == '__main__':
    test_array = [5, 2, 3, 1]
    print(sortArray(test_array))

"""
Intuition
My first thought was to implement a insertion sort but I later realize that the time complexity would be O(n^2). To get a more efficient algorithm, I used a merge sort algorithm to divide and conquer the sorting of subarrays.

Approach
Base case would be if the the array or sub-array's size is less than or equal to 1 element. Then, the algorithm divide the array to almost equal parts. Then the function would call upon itself but for each subarray. Continuing down to the merge section, we use pointers for the left, right and merged array labled as i,j, and k respectively. While both array's index are within bounds, the function compares the left array's value at index with the right array's value. If left is less than or equal to the right, then the left array value will be merged to the main array. If not, the right will be merged into the main array. (Using less than or equal to for the comparison will perserve the order of equal values, creating a stable sort). The index of the array used and the main array will increment. This will repeat until one subarray is complete. Then the function will find the remaining subarray and merge the values back into the main array.

Time complexity: O(n logn)
Since we are dividing and conquering the array using recursion to sort, the time complexity of that particular function will be log(n). However, since the the comparison/insertion function will iterate through all the values, the time complexity will be O(n). So overall, the time complexity of the whole function will be O(n logn)

Space complexity:O(n)
The function will create arrays equal to the length of the inputted array so the space complexity of th O(n)
"""
