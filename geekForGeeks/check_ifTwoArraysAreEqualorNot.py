class Solution:
    def check(self, arr1, arr2):
        mp = {}
        if len(arr1) != len(arr2):
            return False
        for num in arr1:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1

class Solution:
    def check(self, arr1, arr2):
        if len(arr1) != len(arr2):
            return False
        freq1 = {}
        freq2 = {}

        for num in arr1:
                freq1[num] = freq1.get(num, 0) + 1
        for num in arr2:
            freq2[num] = freq2.get(num, 0) + 1
        return freq1 == freq2