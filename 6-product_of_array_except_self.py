'''

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)

'''






nums = [1,2,3,4]
prefix = []
suffix = [1] * len(nums)
result = [0] * len(nums)

print(nums)
#prefix
for i in range(len(nums)):
    if i == 0:
        prefix.append(nums[i])
    else:
        prefix.append(prefix[i-1] * nums[i])

print(prefix)

#suffix
for i in range(len(nums) - 1, -1, -1):
    if(i == len(nums)-1):
        suffix[i] = nums[i]
    else:
        suffix[i] = suffix[i+1] * nums[i]

print(suffix)

for i in range(len(nums)):
    if(i == 0):
        result[i] = suffix[i+1]
    elif(i == len(nums)-1):
        result[i] = prefix[i-1]
    else:
        result[i] = prefix[i-1] * suffix[i+1]
    
print(result)