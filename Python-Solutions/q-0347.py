"""
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/description/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
import collections


def topKFrequent(nums: list[int], k: int) -> list[int]:
        num_counter = collections.defaultdict(int)
        output = []

        for element in nums:
            num_counter[element] += 1

        for itr in range(k):
            get_max = max(num_counter,key=num_counter.get)
            output.append(get_max)
            num_counter.pop(max(num_counter,key=num_counter.get))
        return output

if __name__ == '__main__':
    test = [1,1,1,2,2,3]
    k_value = 2

    print(topKFrequent(test, k_value))

"""
Intuition
My thoughts going into this problem was to create a dictionary with a counter with the frequencies of each number in the list 'nums'. From there, I would retrieve the max key value of all the keys, place it into a list, then delete the dictionary element and repeat if the k is greater than 1.

Approach
Using the defaultdict, I create a dictionary with the keys being the numbers found in 'nums' list and an int value for the values as the count of instances. After completing the dictionary, the functions loops 'k' times where it finds the max value of all the keys and inserts it into the list 'output'. It then pops the key-value pair to avoid duplicates.

Time complexity: O(n*k) or O(n^2)
Since the function iterates through all the elements once to create the 'num_counter' dictionary, that operates at O(n), where 'n' is the amount of elements in the 'nums' list. However, there is another loop where it will excute 'k' times getting the max value and deleting the max value in the 'num_counter' dictionary. There for, O(n*k) or in the worst case where k is equal to n, O(n^2)

Space complexity:O(n)
The function's use of space increases linearly to the amount of elements in 'nums' list, or 'n'. The output list does not count as it is required space to answer the question and does not use extra space. Therefore, the space complexity is O(n).
"""