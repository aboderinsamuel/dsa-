class Solution:
    def twoSum(self, nums, target):
        notebook = {} #Hashmap to store numbers and positions
        for i, num in enumerate(nums):
            complement = target - num
            if complement in notebook:
                return [notebook[complement], i]
            notebook[num] = i