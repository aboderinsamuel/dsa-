class Solution:
    def twoSum(self, nums, target):
        notebook = {} #Hashmap to store numbers and positions
        for i, num in enumerate(nums):
            complement = target - num
            if complement in notebook:
                return [notebook[complement], i]
            notebook[num] = i

solution = Solution()

nums = [2,3,4,5,6]
target = 8

output = solution.twoSum(nums, target)
print(output)
