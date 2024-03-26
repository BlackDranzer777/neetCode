def firstMissingPositive(nums):
    for i in range(0, len(nums)):
        if nums[i] < 0:
            nums[i] = 0

    print("After loop 1 : ", nums)
    
    # [3,-3,6,3]
    for n in nums:
        index = abs(n) - 1
        if 1 <= index+1 <= len(nums):
            # print(n)
            if nums[index] == 0:
                nums[index] = (len(nums) + 1) * -1
            elif nums[index] > 0:
                nums[index] = nums[index] * -1
            else:
                continue
    
    print("After loop 2 : ", nums)

    for i in range(1, len(nums)+1):
        index = i - 1
        if nums[index] >= 0:
            return i
    
    return len(nums) + 1
        
    print("After loop 3 : ", nums)
        
a = [1,2,5,4,3,6, 7]
missing_number = firstMissingPositive(a)
print(missing_number)