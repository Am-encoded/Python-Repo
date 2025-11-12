"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def two_sum(nums, target):
    """
    brute force method
    """
    #use a nested loop to check every pair in list to see if their sum is equal to th target value and return their indices;
    #for i in range(len(nums)):
    #   for j in range(i + 1, len(nums)-1):
    #        if nums[i] + nums[j] == target:
    #            return [i, j]
    #return []

    """
    hash map method: dictionary
    """
    #initialiize an empty dictionary that will store integer and their indexes as key value pair;
    pair_idx = {}
    #iterate through every value in list with their indexes enumerate() function helps with it;
    #"i" is index of the value "num";
    for i, num in enumerate(nums):
        #check if the complementary exists in the hash map;
        if target - num in pair_idx:
            #store the value if pair is found;
            return [pair_idx[target - num], i]
        #if pair is not found store the index in dictionary so we can look up to it later;
        pair_idx[num] = i
    return []


print(two_sum([2, 7, 11, 15], 9))