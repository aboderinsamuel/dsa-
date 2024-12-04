class Solution:
    def maxProd(self, arr):
        largest = second_largest = float('-inf')
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest:
                second_largest = num
        return largest * second_largest

solution = Solution()
arr = [2,3,7,8,9,10]
printNum = solution.maxProd(arr)
print(printNum)