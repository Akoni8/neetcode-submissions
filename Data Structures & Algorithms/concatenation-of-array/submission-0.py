class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        size = len(nums)
        for i in range(0, size) :
            ans.insert(i, nums[i])
            ans.insert(i+size, nums[i])
        return ans