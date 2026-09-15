# LeetCode Question 1
# Two Sum

# Question:
# Given an array of integers nums and an integer target,
# return the indices of the two numbers such that they add up to target.
#
# You may assume that each input has exactly one solution,
# and you may not use the same element twice.
#
# Example:
# nums = [2, 7, 11, 15]
# target = 9
# Output: [0, 1]


# Solution:

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i


# Time Complexity: O(n)
# Space Complexity: O(n)


# LeetCode Question 26
# Remove Duplicates from Sorted Array

# Question:
# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element
# appears only once.
#
# Return the number of unique elements.
#
# Example:
# nums = [1, 1, 2]
# Output: 2
#
# After removing duplicates:
# nums = [1, 2, ...]


# Solution:

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


# Time Complexity: O(n)
# Space Complexity: O(1)