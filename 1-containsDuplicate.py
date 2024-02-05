nums = [1,2,3,4,5]

def checkDuplicate(nums):
    #Create a hash set
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

print(checkDuplicate(nums))