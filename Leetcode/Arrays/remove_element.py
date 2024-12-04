class Solution(object):
    def removeElement(self, nums, val):
        k = 0 #Pointer for placing no-val elements
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k]  = nums[i] #Place the non-val elements at the front
                k +=1
        return k
solution = Solution()
nums = [3,2,2,3]
val = 3
k = solution.removeElement(nums, val)


print(f"Updated Array: {nums[:k]}")
print(F"Number of elements not equal to {val}: {k}")