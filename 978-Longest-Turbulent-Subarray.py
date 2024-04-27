class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        R, L = 1, 0
        maxLength, prevSign = 1, ""

        while R < len(arr):
            if arr[R] > arr[R - 1] and prevSign != ">":
                maxLength = max(maxLength, R - L + 1)
                R += 1
                prevSign = ">"
                
            elif arr[R] < arr[R - 1] and prevSign != "<":
                maxLength = max(maxLength, R - L + 1)
                R += 1
                prevSign = "<"

            else:
                R = R + 1 if arr[R] == arr[R - 1] else R
                L = R - 1
                prevSign = ""

        return maxLength