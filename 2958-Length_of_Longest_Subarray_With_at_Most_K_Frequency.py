#Use Sliding window Algorithm

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hashMap = {}
        left = 0
        lengthOfArray = 0
        maxLength = 0
        for right in range(len(nums)):
            if nums[right] in hashMap:
                hashMap[nums[right]] += 1
            else:
                hashMap[nums[right]] = 1
            while hashMap[nums[right]] > k:
                hashMap[nums[left]] -= 1
                left += 1
            lengthOfArray = right - left + 1
            maxLength = max(maxLength, lengthOfArray)
        return maxLength