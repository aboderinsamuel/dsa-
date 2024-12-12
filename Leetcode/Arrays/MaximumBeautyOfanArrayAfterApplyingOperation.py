from typing import List
class Solution:
    def maxBeauty(self, nums:List[int], k:int) -> int:
#Using Sweep line algorithm
        events = []
        for num in nums:
            events.append((num-k, True))
            events.append((num+k+1, False)) # ranges are inclusive
        # Max intersection
        events.sort()
        count, maxCount = 0, 0
        for pos, isStart in events:
            if isStart:
                count += 1
            else:
                count -= 1
            maxCount = max(maxCount, count)
        return maxCount

                #OR

class Solution(object):
    def maximumBeauty(self, nums, k):
    # Sort the array to manage ranges efficiently
        nums.sort()
        n = len(nums)
        max_beauty = 0
        left = 0
    
    # Sliding window approach
        for right in range(n):
        # Ensure the window satisfies the range constraint
            while nums[right] - nums[left] > 2 * k:
                left += 1
        # Update maximum beauty (size of current window)
            max_beauty = max(max_beauty, right - left + 1)
    
        return max_beauty
    
