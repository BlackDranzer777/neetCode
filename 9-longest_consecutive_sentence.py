nums = [100,4,200,1,3,2]
hash = set(nums)
longest = 0

for element in nums:
    number = element
    if element-1 not in hash:
        length=0
        while number in hash:
            length+=1
            number=number+1

        longest = max(length, longest)

print(longest)