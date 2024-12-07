class Solution:
    def arrStringsAreEqual(self, arr1, arr2):
        concat_word1 = "".join(arr1)
        concat_word2 = "".join(arr2)

        return concat_word1 == concat_word2