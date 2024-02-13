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


nums = [-1,1,0,-3,3]
product = 1
count = 0
for number in nums:
    if(number != 0):
        count+=1
        product = product*number

if count > 0:
    product_array = []
    for i in range(len(nums)):
        if nums[i] != 0:
            product_array.append(int(product/nums[i]))
        else:
            product_array.append(product)

    print(product_array)
else:
    product_array = []*len(nums)
