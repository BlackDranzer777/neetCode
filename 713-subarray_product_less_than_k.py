class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #nums = [10 5 2 6], k = 100  
        left = 0
        product = 1
        res = 0
        for right in range(len(nums)):
            product = product*nums[right]
            while product >= k and right >= left:
                product = product // nums[left]
                left = left + 1 
            res = res + (right - left + 1)
        return res