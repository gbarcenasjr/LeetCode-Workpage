"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""


def longestConsecutive(nums: list[int]) -> int:
    longest = 0
    num_set = set(nums)

    for number in num_set:
        if number - 1 not in num_set:
            current_number = number
            current_streak = 1

            while current_number + 1 in num_set:
                current_number += 1
                current_streak += 1

            longest = max(longest, current_streak)

    return longest

"""
Intuition
The goal is to find the longest consecutive sequence of numbers in a given list. To solve this problem efficiently, 
one can leverage the properties of sets to achieve O(1) time complexity for querying the presence of an element.

Approach
1. Convert the given list of numbers, `nums`, into a set (`num_set`) to achieve O(1) look-up times.
2. For each `number` in `num_set`, check if it's the start of a sequence. This is done by ensuring the previous number 
   (`number - 1`) is not in the set. This step ensures we don't count duplicates and ensures we only count each sequence 
   once.
3. If the `number` is the start of a sequence, loop to count how many numbers are in this sequence using a while loop.
4. Keep track of the longest sequence found.

Implementation Notes
- By using sets, the look-up is efficient.
- The check `number - 1 not in num_set` ensures that for a sequence like [1,2,3,4,5], only when we hit the number 1, 
  will we start counting the sequence. For other numbers, this check will prevent unnecessary counting.
- The inner while loop increments the `current_number` and counts the sequence until the next number isn't found in the 
  set.

Time Complexity: O(n)
Though there's a nested loop structure, in the worst-case scenario, each number will be checked once as a start of a 
sequence and then checked once again in the inner loop as part of some sequence. Thus, the operations inside the loops 
are O(n).

Space Complexity: O(n)
An additional set, `num_set`, is created which can, in the worst case, have all n numbers from the original list.
"""