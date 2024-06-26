# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        global mid
        while l<r:
            mid = (l+r)//2
            if isBadVersion(mid) == False:
                l = mid+1
            elif isBadVersion(mid) == True:
                r = mid
        return r