nums = [1,2,3,5,7,6,4,7]

slow2, slow, fast = 0,0,0
while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
        break

while True:
    slow2 = nums[slow2]
    slow = nums[slow]
    if slow == slow2:
        break

print(slow)