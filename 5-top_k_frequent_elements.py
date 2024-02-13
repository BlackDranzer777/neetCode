'''

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''

nums = [1,1,1,2,2,3, 444, 444, 444, 444, 55, 55, 55, 55]
k = 2

number_frequency = {}

k_elements = []

for number in nums:
    if number in number_frequency:
        number_frequency[number] +=1
    else:
        number_frequency[number] = 1

number_frequency_sorted = dict(sorted(number_frequency.items(), key=lambda item: item[1], reverse=True))
print(number_frequency_sorted)

for key in number_frequency_sorted:
    print(key)
    if(len(k_elements) < k):
        k_elements.append(key)

print(k_elements)