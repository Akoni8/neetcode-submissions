class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num1 in range(0, len(nums)):
            for num2 in range(num1+1, len(nums)):
                if (nums[num1] == nums[num2]):
                    return True
        return False
         